---
title: "MapFeatureModes (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapfeaturemodes"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapFeatureModes

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapFeatureModes
------------------------------------------------------------------------
public final class MapFeatureModes extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Holds constants for map feature modes, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)).

Use [`DEFAULT`](#DEFAULT) to enable a feature with its default mode.

Note: The default mode is defined by the currently loaded map scene configuration and may vary per [`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview"). The currently active features and modes can be inspected using [`MapScene.getActiveFeatures()`](sdk-for-android-explore-api-reference-latestmapscene#getActiveFeatures()) after the scene is loaded.

See [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview") for constants representing the feature names.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [AMBIENT_OCCLUSION_ALL](#AMBIENT_OCCLUSION_ALL)

Ambient occlusion effect is shown for extruded buildings and landmarks.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUILDING_FOOTPRINTS_ALL](#BUILDING_FOOTPRINTS_ALL)

All building footprints are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [CONGESTION_ZONES_ALL](#CONGESTION_ZONES_ALL)

All congestion zones are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [DEFAULT](#DEFAULT)

Enables the default mode of a map feature.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ENVIRONMENTAL_ZONES_ALL](#ENVIRONMENTAL_ZONES_ALL)

All environmental zones are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [EXTRUDED_BUILDINGS_ALL](#EXTRUDED_BUILDINGS_ALL)

All extruded buildings are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [LOW_SPEED_ZONES_ALL](#LOW_SPEED_ZONES_ALL)

All low speed zones are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ROAD_EXIT_LABELS_ALL](#ROAD_EXIT_LABELS_ALL)

Road exit labels are shown with numbers and names, if available.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ROAD_EXIT_LABELS_NUMBERS_ONLY](#ROAD_EXIT_LABELS_NUMBERS_ONLY)

Road exit labels are shown with numbers, if available.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHADOWS_ALL](#SHADOWS_ALL)

Shadows are shown for extruded buildings and landmarks.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW](#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW)

Only available when Japan map is used.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_FLOW_WITH_FREE_FLOW](#TRAFFIC_FLOW_WITH_FREE_FLOW)

Traffic flow shows green lines when there is no traffic congestion.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_FLOW_WITHOUT_FREE_FLOW](#TRAFFIC_FLOW_WITHOUT_FREE_FLOW)

Traffic flow does not show green lines when there is no traffic congestion.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_INCIDENTS_ALL](#TRAFFIC_INCIDENTS_ALL)

All available traffic incidents are shown.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_LIGHTS_ALL](#TRAFFIC_LIGHTS_ALL)

All available traffic lights are shown.

## Constructor Summary

Constructors

Constructor

  Description

  [MapFeatureModes](#%3Cinit%3E())`()`

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### DEFAULT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEFAULT

    Enables the default mode of a map feature. Can be used with any map feature.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.DEFAULT)

### BUILDING_FOOTPRINTS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUILDING_FOOTPRINTS_ALL

    All building footprints are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.BUILDING_FOOTPRINTS_ALL)

### CONGESTION_ZONES_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONGESTION_ZONES_ALL

    All congestion zones are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.CONGESTION_ZONES_ALL)

### EXTRUDED_BUILDINGS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXTRUDED_BUILDINGS_ALL

    All extruded buildings are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.EXTRUDED_BUILDINGS_ALL)

### ENVIRONMENTAL_ZONES_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENVIRONMENTAL_ZONES_ALL

    All environmental zones are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.ENVIRONMENTAL_ZONES_ALL)

### LOW_SPEED_ZONES_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOW_SPEED_ZONES_ALL

    All low speed zones are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.LOW_SPEED_ZONES_ALL)

### TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW

    Only available when Japan map is used.

    Traffic flow shows green lines depending on the region.

    In Japan green lines will not be shown, as if the [`TRAFFIC_FLOW_WITHOUT_FREE_FLOW`](#TRAFFIC_FLOW_WITHOUT_FREE_FLOW) were used.

    In rest of the world, green lines will be shown, as if the [`TRAFFIC_FLOW_WITH_FREE_FLOW`](#TRAFFIC_FLOW_WITH_FREE_FLOW) were used.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW)

### TRAFFIC_FLOW_WITH_FREE_FLOW

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_FLOW_WITH_FREE_FLOW

    Traffic flow shows green lines when there is no traffic congestion.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW)

### TRAFFIC_FLOW_WITHOUT_FREE_FLOW

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_FLOW_WITHOUT_FREE_FLOW

    Traffic flow does not show green lines when there is no traffic congestion.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW)

### TRAFFIC_INCIDENTS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_INCIDENTS_ALL

    All available traffic incidents are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_INCIDENTS_ALL)

### TRAFFIC_LIGHTS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_LIGHTS_ALL

    All available traffic lights are shown.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_LIGHTS_ALL)

### ROAD_EXIT_LABELS_NUMBERS_ONLY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ROAD_EXIT_LABELS_NUMBERS_ONLY

    Road exit labels are shown with numbers, if available.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY)

### ROAD_EXIT_LABELS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ROAD_EXIT_LABELS_ALL

    Road exit labels are shown with numbers and names, if available.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_ALL)

### SHADOWS_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHADOWS_ALL

    Shadows are shown for extruded buildings and landmarks.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.SHADOWS_ALL)

### AMBIENT_OCCLUSION_ALL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AMBIENT_OCCLUSION_ALL

    Ambient occlusion effect is shown for extruded buildings and landmarks.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatureModes.AMBIENT_OCCLUSION_ALL)

## Constructor Details

  - ()" class="section detail">

### MapFeatureModes

public MapFeatureModes()
