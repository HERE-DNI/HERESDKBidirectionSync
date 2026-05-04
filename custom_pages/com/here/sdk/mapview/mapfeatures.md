---
title: "MapFeatures (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapfeatures"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapFeatures

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapFeatures
------------------------------------------------------------------------
public final class MapFeatures extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Holds constants for map features, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) and [`MapScene.disableFeatures(java.util.List<java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#disableFeatures(java.util.List)).

See [`MapFeatureModes`](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview") for constants representing feature modes.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [AMBIENT_OCCLUSION](#AMBIENT_OCCLUSION)

Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUILDING_FOOTPRINTS](#BUILDING_FOOTPRINTS)

The 2D footprint of buildings.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [CONGESTION_ZONES](#CONGESTION_ZONES)

City areas designated as congestion zones (or congestion charge zones), which impose fees on entering such areas.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ENVIRONMENTAL_ZONES](#ENVIRONMENTAL_ZONES)

City areas designated as environmental zones, which empose limitations on the type of vehicles that are allowed to enter such areas.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [EXTRUDED_BUILDINGS](#EXTRUDED_BUILDINGS)

Simple 3D representation of buildings.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [LOW_SPEED_ZONES](#LOW_SPEED_ZONES)

City areas designated as low speed zones.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ROAD_EXIT_LABELS](#ROAD_EXIT_LABELS)

Show or hide road exit labels, if available.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHADOWS](#SHADOWS)

Shadows for all building types (extruded buildings and landmarks).

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_FLOW](#TRAFFIC_FLOW)

Traffic flow speed.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_INCIDENTS](#TRAFFIC_INCIDENTS)

Traffic incidents.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRAFFIC_LIGHTS](#TRAFFIC_LIGHTS)

Traffic lights.

## Constructor Summary

Constructors

Constructor

  Description

  [MapFeatures](#%3Cinit%3E())`()`

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### EXTRUDED_BUILDINGS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EXTRUDED_BUILDINGS

    Simple 3D representation of buildings.

    Supports only one mode: [`MapFeatureModes.EXTRUDED_BUILDINGS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#EXTRUDED_BUILDINGS_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY), [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT) and all hybrid schemes: [`MapScheme.HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_DAY) [`MapScheme.HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_NIGHT), [`MapScheme.LITE_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_DAY) [`MapScheme.LITE_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_NIGHT), [`MapScheme.LOGISTICS_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_DAY) and [`MapScheme.LOGISTICS_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_NIGHT).

    By default, extruded buildings are enabled on all compatible map schemes.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.EXTRUDED_BUILDINGS)

### BUILDING_FOOTPRINTS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUILDING_FOOTPRINTS

    The 2D footprint of buildings.

    Supports only one mode: [`MapFeatureModes.BUILDING_FOOTPRINTS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#BUILDING_FOOTPRINTS_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY), [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT) and all hybrid schemes: [`MapScheme.HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_DAY) [`MapScheme.HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_NIGHT), [`MapScheme.LITE_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_DAY) [`MapScheme.LITE_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_NIGHT), [`MapScheme.LOGISTICS_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_DAY) and [`MapScheme.LOGISTICS_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_NIGHT).

    By default, building footprints are enabled on all compatible map schemes.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.BUILDING_FOOTPRINTS)

### TRAFFIC_FLOW

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_FLOW

    Traffic flow speed. An online connection is required for the traffic flow to be shown.

    If the offline-mode is enabled for offline maps usage, the live traffic flow can still be shown in offline mode by enabling pass-through feature for traffic flow on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

    Supported modes:

    - [`MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW),
    - [`MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW),
    - [`MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW).

    Default mode is [`MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT). By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_FLOW)

### TRAFFIC_INCIDENTS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_INCIDENTS

    Traffic incidents. An online connection is required for the traffic incidents to be shown.

    If the offline-mode is enabled for offline maps usage, the live traffic incidents can still be shown in offline mode by enabling pass-through feature for traffic incidents on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

    Supports only one mode: [`MapFeatureModes.TRAFFIC_INCIDENTS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_INCIDENTS_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT). By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS)

### TRAFFIC_LIGHTS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRAFFIC_LIGHTS

    Traffic lights.

    Supports only one mode: [`MapFeatureModes.TRAFFIC_LIGHTS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#TRAFFIC_LIGHTS_ALL)

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT).

    By default, traffic lights are enabled on all compatible map schemes.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_LIGHTS)

### ENVIRONMENTAL_ZONES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ENVIRONMENTAL_ZONES

    City areas designated as environmental zones, which empose limitations on the type of vehicles that are allowed to enter such areas.

    Supports only one mode: [`MapFeatureModes.ENVIRONMENTAL_ZONES_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ENVIRONMENTAL_ZONES_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT). By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.ENVIRONMENTAL_ZONES)

### CONGESTION_ZONES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONGESTION_ZONES

    City areas designated as congestion zones (or congestion charge zones), which impose fees on entering such areas.

    Supports only one mode: [`MapFeatureModes.CONGESTION_ZONES_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#CONGESTION_ZONES_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT). By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.CONGESTION_ZONES)

### LOW_SPEED_ZONES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOW_SPEED_ZONES

    City areas designated as low speed zones. Only available when Japan map is used.

    Supports only one mode: [`MapFeatureModes.LOW_SPEED_ZONES_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#LOW_SPEED_ZONES_ALL).

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT). By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.LOW_SPEED_ZONES)

### ROAD_EXIT_LABELS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ROAD_EXIT_LABELS

    Show or hide road exit labels, if available.

    Supported modes: [`MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY), [`MapFeatureModes.ROAD_EXIT_LABELS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ROAD_EXIT_LABELS_ALL)

    Default mode is [`MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY).

    Road exit labels are enabled by default with [`MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY) on normal, lite and topo schemes and with [`MapFeatureModes.ROAD_EXIT_LABELS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#ROAD_EXIT_LABELS_ALL) on logistics schemes. Note that topo schemes are only available in the HERE SDK Navigate variant.

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY) and [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT).
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.ROAD_EXIT_LABELS)

### SHADOWS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHADOWS

    Shadows for all building types (extruded buildings and landmarks).

    Supports only one mode: [`MapFeatureModes.SHADOWS_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#SHADOWS_ALL).

    A [`ShadowQuality`](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview") must be set on the MapContext through a MapView or the feature has no effect.

    Shadows have a performance impact and should be considered only for devices with sufficient performance.

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY), [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT) and all hybrid schemes: [`MapScheme.HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_DAY) [`MapScheme.HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_NIGHT), [`MapScheme.LITE_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_DAY) [`MapScheme.LITE_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_NIGHT), [`MapScheme.LOGISTICS_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_DAY) and [`MapScheme.LOGISTICS_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_NIGHT).

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.SHADOWS)

### AMBIENT_OCCLUSION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AMBIENT_OCCLUSION

    Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).

    Supports only one mode: [`MapFeatureModes.AMBIENT_OCCLUSION_ALL`](sdk-for-android-explore-api-reference-latestmapfeaturemodes#AMBIENT_OCCLUSION_ALL).

    This visual effect has a performance impact and should be considered only for devices with sufficient performance.

    Not supported for [`MapScheme.SATELLITE`](sdk-for-android-explore-api-reference-latestmapscheme#SATELLITE), [`MapScheme.ROAD_NETWORK_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_DAY), [`MapScheme.ROAD_NETWORK_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#ROAD_NETWORK_NIGHT) and all hybrid schemes: [`MapScheme.HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_DAY) [`MapScheme.HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#HYBRID_NIGHT), [`MapScheme.LITE_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_DAY) [`MapScheme.LITE_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LITE_HYBRID_NIGHT), [`MapScheme.LOGISTICS_HYBRID_DAY`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_DAY) and [`MapScheme.LOGISTICS_HYBRID_NIGHT`](sdk-for-android-explore-api-reference-latestmapscheme#LOGISTICS_HYBRID_NIGHT).

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapFeatures.AMBIENT_OCCLUSION)

## Constructor Details

  - ()" class="section detail">

### MapFeatures

public MapFeatures()
