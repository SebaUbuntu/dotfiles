#!/usr/bin/env python
#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from argparse import ArgumentParser
from enum import Enum
from pathlib import Path
from typing import List, Iterable, Optional
from xml.etree import ElementTree

class DynamicRange(Enum):
	SDR = "sdr"
	HDR = "hdr"

class ColorGamut(Enum):
	NATIVE = "native"
	SRGB = "srgb"
	DCI_P3 = "dcip3"

class PictureQuality(Enum):
	STANDARD = "standard"
	ENHANCED = "enhanced"

class Mode:
	def __init__(
		self,
		name: str,
		dynamic_range: DynamicRange,
		color_gamut: ColorGamut,
		picture_quality: Optional[PictureQuality],
		features: Iterable[int],
	):
		self.name = name
		self.dynamic_range = dynamic_range
		self.color_gamut = color_gamut
		self.picture_quality = picture_quality
		self.features = frozenset(features)

	def __str__(self) -> str:
		return (
			f"Name: {self.name}"
			f", dynamic range: {self.dynamic_range}"
			f", color gamut: {self.color_gamut}"
			f", picture quality: {self.picture_quality}"
			f", features: {self.features}"
		)

class CalibrationData:
	def __init__(
		self,
		modes: List[Mode],
		default_mode: int = 0,
	):
		self.modes = modes or []
		self.default_mode = default_mode

	@classmethod
	def from_xml(cls, xml: Path) -> "CalibrationData":
		root = ElementTree.fromstring(xml.read_text())

		disp_modes = root.find("Disp_Modes")
		assert disp_modes is not None, "Disp_Modes element not found"

		default_mode = int(disp_modes.attrib["DefaultMode"])

		modes = []

		for i, mode in enumerate(disp_modes):
			mode_id = int(mode.attrib["ModeID"])
			assert mode_id == i, (
				f"Mode ID {mode_id} does not match expected {i}, "
				"mode IDs must be sequential and start at 0."
			)

			num_features = int(mode.attrib["NumOfFeatures"])
			assert num_features == len(mode) + 6, \
				f"Wrong number of features {num_features} for mode ID {mode_id}, expected {len(mode) + 6}, got {num_features}"

			picture_quality = mode.attrib.get("PictureQuality")

			modes.append(
				Mode(
					name=mode.attrib["Name"],
					dynamic_range=DynamicRange(mode.attrib["DynamicRange"]),
					color_gamut=ColorGamut(mode.attrib["ColorGamut"]),
					picture_quality=PictureQuality(picture_quality) if picture_quality else None,
					features=[int(feature.attrib["FeatureType"]) for feature in mode],
				)
			)

		return cls(modes=modes, default_mode=default_mode)

MODELS = {
	"sm8150": CalibrationData(
		default_mode=0,
		modes=[
			# qdcm_calib_data_default.xml
			Mode(
				name="native",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.NATIVE,
				picture_quality=None,
				features=[
					2,
					3,
					7,
					8,
					14,
					20,
					22,
				],
			),
			Mode(
				name="HDR",
				dynamic_range=DynamicRange.HDR,
				color_gamut=ColorGamut.DCI_P3,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					4,
					7,
					8,
					14,
					20,
					22,
					28,
				],
			),
			Mode(
				name="P3",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.DCI_P3,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					4,
					7,
					8,
					14,
					20,
					22,
				],
			),
			Mode(
				name="sRGB",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.SRGB,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					7,
					8,
					14,
					20,
					22,
				],
			),
		],
	),
	"sm8250": CalibrationData(
		default_mode=0,
		modes=[
			# qdcm_calib_data_default.xml
			Mode(
				name="native",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.NATIVE,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					7,
					8,
					14,
					20,
					22,
				],
			),
			Mode(
				name="HDR",
				dynamic_range=DynamicRange.HDR,
				color_gamut=ColorGamut.DCI_P3,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					4,
					7,
					8,
					14,
					20,
					22,
					28,
				],
			),
			Mode(
				name="P3",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.DCI_P3,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					4,
					7,
					8,
					14,
					20,
					22,
				],
			),
			Mode(
				name="sRGB",
				dynamic_range=DynamicRange.SDR,
				color_gamut=ColorGamut.SRGB,
				picture_quality=PictureQuality.STANDARD,
				features=[
					2,
					3,
					7,
					8,
					14,
					20,
					22,
				],
			),
		],
	),
}

def main():
	parser = ArgumentParser()
	parser.add_argument("xml", type=Path, help="Path to the calibration data XML file")
	parser.add_argument("platform", choices=MODELS.keys(), help="Platform name to check calibration data against")
	args = parser.parse_args()

	calibration_data = CalibrationData.from_xml(args.xml)
	platform_model = MODELS[args.platform]

	assert calibration_data.default_mode == platform_model.default_mode, \
		"Calibration data has a different default mode than the selected model"

	assert len(calibration_data.modes) == len(platform_model.modes), \
		"Calibration data has a different number of modes than the selected model"

	for i in range(len(calibration_data.modes)):
		model_mode = platform_model.modes[i]
		calibration_mode = calibration_data.modes[i]

		assert model_mode.name == calibration_mode.name, \
			f"Mode {i} has a different name than the selected model, expected {model_mode.name}, got {calibration_mode.name}"
		assert model_mode.dynamic_range == calibration_mode.dynamic_range, \
			f"Mode {i} has a different dynamic range than the selected model, expected {model_mode.dynamic_range}, got {calibration_mode.dynamic_range}"
		assert model_mode.color_gamut == calibration_mode.color_gamut, \
			f"Mode {i} has a different color gamut than the selected model, expected {model_mode.color_gamut}, got {calibration_mode.color_gamut}"
		assert model_mode.picture_quality == calibration_mode.picture_quality, \
			f"Mode {i} has a different picture quality than the selected model, expected {model_mode.picture_quality}, got {calibration_mode.picture_quality}"

		assert len(model_mode.features) == len(calibration_mode.features), \
			f"Mode {i} has a different number of features than the selected model"

		for feature_type in calibration_mode.features:
			assert feature_type in model_mode.features, \
				f"Mode {i} has an unknown feature {feature_type}"

		print(f"Mode {i} matches the selected model")

	print("Calibration data matches the selected model")

main()
