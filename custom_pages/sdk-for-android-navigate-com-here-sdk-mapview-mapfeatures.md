---
title: "MapFeatures (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.MapFeatures → com.here.sdk.mapview.MapFeatures

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapFeatures</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Holds constants for map features, to be used with MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) and MapScene.disableFeatures(java.util.List\<java.lang.String\>) . See MapFeatureModes for constants representing feature modes.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#AMBIENT_OCCLUSION" class="member-name-link"><code>AMBIENT_OCCLUSION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#BUILDING_FOOTPRINTS" class="member-name-link"><code>BUILDING_FOOTPRINTS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The 2D footprint of buildings.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#CONGESTION_ZONES" class="member-name-link"><code>CONGESTION_ZONES</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  City areas designated as congestion zones (or congestion charge zones), which impose fees on entering such areas.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#CONTOURS" class="member-name-link"><code>CONTOURS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Show or hide contour lines on the map to represent elevation changes.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#ENVIRONMENTAL_ZONES" class="member-name-link"><code>ENVIRONMENTAL_ZONES</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  City areas designated as environmental zones, which empose limitations on the type of vehicles that are allowed to enter such areas.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#EXTRUDED_BUILDINGS" class="member-name-link"><code>EXTRUDED_BUILDINGS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Simple 3D representation of buildings.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#LANDMARKS" class="member-name-link"><code>LANDMARKS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Displays 3D landmarks on the map.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#LOW_SPEED_ZONES" class="member-name-link"><code>LOW_SPEED_ZONES</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  City areas designated as low speed zones.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#PUBLIC_TRANSIT" class="member-name-link"><code>PUBLIC_TRANSIT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Toggles the display of public transit lines for systems like subway, tram, train, monorail, and ferry, based on the selected mode.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#ROAD_EXIT_LABELS" class="member-name-link"><code>ROAD_EXIT_LABELS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Show or hide road exit labels, if available.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#SAFETY_CAMERAS" class="member-name-link"><code>SAFETY_CAMERAS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Safety and speed cameras.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#SHADOWS" class="member-name-link"><code>SHADOWS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Shadows for all building types (extruded buildings and landmarks).

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TERRAIN" class="member-name-link"><code>TERRAIN</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Show elevation topography.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_FLOW" class="member-name-link"><code>TRAFFIC_FLOW</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic flow speed.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_INCIDENTS" class="member-name-link"><code>TRAFFIC_INCIDENTS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic incidents.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_LIGHTS" class="member-name-link"><code>TRAFFIC_LIGHTS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic lights.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRUCK_PREFERRED_ROADS" class="member-name-link"><code>TRUCK_PREFERRED_ROADS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Show or hide truck preferred road

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#VEHICLE_RESTRICTIONS" class="member-name-link"><code>VEHICLE_RESTRICTIONS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Vehicle restrictions.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      MapFeatures ()

  </div>

  <div class="col-last even-row-color">

   

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-EXTRUDED_BUILDINGS" class="section detail">

    ### EXTRUDED_BUILDINGS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTRUDED_BUILDINGS</span>

    </div>

    <div class="block">

    Simple 3D representation of buildings. Supports only one mode: MapFeatureModes.EXTRUDED_BUILDINGS_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT . By default, extruded buildings are enabled on all compatible map schemes.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.EXTRUDED_BUILDINGS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-BUILDING_FOOTPRINTS" class="section detail">

    ### BUILDING_FOOTPRINTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDING_FOOTPRINTS</span>

    </div>

    <div class="block">

    The 2D footprint of buildings. Supports only one mode: MapFeatureModes.BUILDING_FOOTPRINTS_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT . By default, building footprints are enabled on all compatible map schemes.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.BUILDING_FOOTPRINTS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_FLOW" class="section detail">

    ### TRAFFIC_FLOW

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW</span>

    </div>

    <div class="block">

    Traffic flow speed. An online connection is required for the traffic flow to be shown. If the offline-mode is enabled for offline maps usage, the live traffic flow can still be shown in offline mode by enabling pass-through feature for traffic flow on sdk.core.engine.SDKNativeEngine . See sdk.core.engine.SDKNativeEngine.pass_through_features for details. Supported modes: MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW , MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW , MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW . Default mode is MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_FLOW">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_INCIDENTS" class="section detail">

    ### TRAFFIC_INCIDENTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_INCIDENTS</span>

    </div>

    <div class="block">

    Traffic incidents. An online connection is required for the traffic incidents to be shown. If the offline-mode is enabled for offline maps usage, the live traffic incidents can still be shown in offline mode by enabling pass-through feature for traffic incidents on sdk.core.engine.SDKNativeEngine . See sdk.core.engine.SDKNativeEngine.pass_through_features for details. Supports only one mode: MapFeatureModes.TRAFFIC_INCIDENTS_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_LIGHTS" class="section detail">

    ### TRAFFIC_LIGHTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_LIGHTS</span>

    </div>

    <div class="block">

    Traffic lights. Supports only one mode: MapFeatureModes.TRAFFIC_LIGHTS_ALL Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, traffic lights are enabled on all compatible map schemes.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_LIGHTS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-VEHICLE_RESTRICTIONS" class="section detail">

    ### VEHICLE_RESTRICTIONS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">VEHICLE_RESTRICTIONS</span>

    </div>

    <div class="block">

    Vehicle restrictions. Requires map version 25 as minimum. If old map data is stored on disk, it might require updating using MapUpdater . Supported modes: MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE , MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE and MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED . Default mode when enabled is MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-SAFETY_CAMERAS" class="section detail">

    ### SAFETY_CAMERAS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SAFETY_CAMERAS</span>

    </div>

    <div class="block">

    Safety and speed cameras. Supports only one mode: MapFeatureModes.SAFETY_CAMERAS_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.SAFETY_CAMERAS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LANDMARKS" class="section detail">

    ### LANDMARKS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LANDMARKS</span>

    </div>

    <div class="block">

    Displays 3D landmarks on the map. Please note: Enabling 3D landmarks with 3D terrain may result in instances where landmarks sink into or float above the terrain. Supported modes: MapFeatureModes.LANDMARKS_TEXTURED , MapFeatureModes.LANDMARKS_GRAYSCALE and MapFeatureModes.LANDMARKS_TEXTURELESS . Default mode is MapFeatureModes.LANDMARKS_GRAYSCALE . By default, 3D landmarks are enabled on all compatible map schemes. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT .

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.LANDMARKS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-ENVIRONMENTAL_ZONES" class="section detail">

    ### ENVIRONMENTAL_ZONES

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ENVIRONMENTAL_ZONES</span>

    </div>

    <div class="block">

    City areas designated as environmental zones, which empose limitations on the type of vehicles that are allowed to enter such areas. Supports only one mode: MapFeatureModes.ENVIRONMENTAL_ZONES_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.ENVIRONMENTAL_ZONES">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-CONGESTION_ZONES" class="section detail">

    ### CONGESTION_ZONES

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CONGESTION_ZONES</span>

    </div>

    <div class="block">

    City areas designated as congestion zones (or congestion charge zones), which impose fees on entering such areas. Supports only one mode: MapFeatureModes.CONGESTION_ZONES_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.CONGESTION_ZONES">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LOW_SPEED_ZONES" class="section detail">

    ### LOW_SPEED_ZONES

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LOW_SPEED_ZONES</span>

    </div>

    <div class="block">

    City areas designated as low speed zones. Only available when Japan map is used. Supports only one mode: MapFeatureModes.LOW_SPEED_ZONES_ALL . Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.LOW_SPEED_ZONES">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TERRAIN" class="section detail">

    ### TERRAIN

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TERRAIN</span>

    </div>

    <div class="block">

    Show elevation topography. Supported modes: MapFeatureModes.TERRAIN_HILLSHADE , MapFeatureModes.TERRAIN_3D . MapFeatureModes.TERRAIN_HILLSHADE is only supported for schemes MapScheme.NORMAL_DAY , MapScheme.NORMAL_NIGHT , MapScheme.LITE_DAY , MapScheme.LITE_NIGHT , MapScheme.LOGISTICS_DAY and MapScheme.LOGISTICS_NIGHT , MapScheme.TOPO_DAY and MapScheme.TOPO_NIGHT . Default mode is MapFeatureModes.TERRAIN_HILLSHADE for the supporting schemes. By default, terrain is disabled, except for MapScheme.TOPO_DAY and MapScheme.TOPO_NIGHT . Note that this feature has performance implications, with extra data use and impact on frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TERRAIN">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-PUBLIC_TRANSIT" class="section detail">

    ### PUBLIC_TRANSIT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">PUBLIC_TRANSIT</span>

    </div>

    <div class="block">

    Toggles the display of public transit lines for systems like subway, tram, train, monorail, and ferry, based on the selected mode. Supported modes: MapFeatureModes.PUBLIC_TRANSIT_ALL , MapFeatureModes.PUBLIC_TRANSIT_ASIA . MapFeatureModes.PUBLIC_TRANSIT_ASIA is supported only when credentials enabled for the enriched Japan map are used. Public transit is disabled by default for all map schemes when using Rest-of-World map data. When using enriched Japan map data, public transit is enabled by default with MapFeatureModes.PUBLIC_TRANSIT_ASIA on normal, lite and topo schemes (including their hybrid variants) and disabled by default on logistics schemes. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.PUBLIC_TRANSIT">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-ROAD_EXIT_LABELS" class="section detail">

    ### ROAD_EXIT_LABELS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS</span>

    </div>

    <div class="block">

    Show or hide road exit labels, if available. Supported modes: MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY , MapFeatureModes.ROAD_EXIT_LABELS_ALL Default mode is MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY . Road exit labels are enabled by default with MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY on normal, lite and topo schemes and with MapFeatureModes.ROAD_EXIT_LABELS_ALL on logistics schemes. Note that topo schemes are only available in the HERE SDK Navigate variant. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT .

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.ROAD_EXIT_LABELS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-SHADOWS" class="section detail">

    ### SHADOWS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SHADOWS</span>

    </div>

    <div class="block">

    Shadows for all building types (extruded buildings and landmarks). Supports only one mode: MapFeatureModes.SHADOWS_ALL . A ShadowQuality must be set on the MapContext through a MapView or the feature has no effect. Shadows have a performance impact and should be considered only for devices with sufficient performance. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.SHADOWS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-AMBIENT_OCCLUSION" class="section detail">

    ### AMBIENT_OCCLUSION

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">AMBIENT_OCCLUSION</span>

    </div>

    <div class="block">

    Ambient occlusion effect for 3D geometries (extruded buildings and landmarks). Supports only one mode: MapFeatureModes.AMBIENT_OCCLUSION_ALL . This visual effect has a performance impact and should be considered only for devices with sufficient performance. Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.AMBIENT_OCCLUSION">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-CONTOURS" class="section detail">

    ### CONTOURS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTOURS</span>

    </div>

    <div class="block">

    Show or hide contour lines on the map to represent elevation changes. Supports only one mode: MapFeatureModes.CONTOURS_ALL Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY , MapScheme.ROAD_NETWORK_NIGHT and all hybrid schemes: MapScheme.HYBRID_DAY MapScheme.HYBRID_NIGHT , MapScheme.LITE_HYBRID_DAY MapScheme.LITE_HYBRID_NIGHT , MapScheme.LOGISTICS_HYBRID_DAY and MapScheme.LOGISTICS_HYBRID_NIGHT . Contours are enabled by default on topo schemes and disabled by default on other schemes.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.CONTOURS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRUCK_PREFERRED_ROADS" class="section detail">

    ### TRUCK_PREFERRED_ROADS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRUCK_PREFERRED_ROADS</span>

    </div>

    <div class="block">

    Show or hide truck preferred road Supported modes: MapFeatureModes.TRUCK_PREFERRED_ROADS_ALL Not supported for MapScheme.SATELLITE , MapScheme.ROAD_NETWORK_DAY and MapScheme.ROAD_NETWORK_NIGHT . By default, this map feature is not enabled.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRUCK_PREFERRED_ROADS">Constant Field Values</a>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### MapFeatures

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapFeatures</span>()

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

