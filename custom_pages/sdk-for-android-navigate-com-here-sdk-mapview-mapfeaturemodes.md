---
title: "MapFeatureModes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.MapFeatureModes → com.here.sdk.mapview.MapFeatureModes

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapFeatureModes</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Holds constants for map feature modes, to be used with MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) . Use DEFAULT to enable a feature with its default mode. Note: The default mode is defined by the currently loaded map scene configuration and may vary per MapScheme . The currently active features and modes can be inspected using MapScene.getActiveFeatures() after the scene is loaded. See MapFeatures for constants representing the feature names.

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

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#AMBIENT_OCCLUSION_ALL" class="member-name-link"><code>AMBIENT_OCCLUSION_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Ambient occlusion effect is shown for extruded buildings and landmarks.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL" class="member-name-link"><code>BUILDING_FOOTPRINTS_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All building footprints are shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#CONGESTION_ZONES_ALL" class="member-name-link"><code>CONGESTION_ZONES_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All congestion zones are shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#CONTOURS_ALL" class="member-name-link"><code>CONTOURS_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Contour lines indicating representing elevation changes are shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#DEFAULT" class="member-name-link"><code>DEFAULT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Enables the default mode of a map feature.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL" class="member-name-link"><code>ENVIRONMENTAL_ZONES_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All environmental zones are shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL" class="member-name-link"><code>EXTRUDED_BUILDINGS_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All extruded buildings are shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_GRAYSCALE" class="member-name-link"><code>LANDMARKS_GRAYSCALE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  3D landmarks are textured with grayscale filter.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_TEXTURED" class="member-name-link"><code>LANDMARKS_TEXTURED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  3D landmarks are textured.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_TEXTURELESS" class="member-name-link"><code>LANDMARKS_TEXTURELESS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  3D landmarks have solid color.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LOW_SPEED_ZONES_ALL" class="member-name-link"><code>LOW_SPEED_ZONES_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All low speed zones are shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#PUBLIC_TRANSIT_ALL" class="member-name-link"><code>PUBLIC_TRANSIT_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Line geometry for all available public transit systems is shown; including subway, tram, train, monorail, ferry and more.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#PUBLIC_TRANSIT_ASIA" class="member-name-link"><code>PUBLIC_TRANSIT_ASIA</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Line geometry for selected public transit systems is shown: subway lines in Japan.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_ALL" class="member-name-link"><code>ROAD_EXIT_LABELS_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Road exit labels are shown with numbers and names, if available.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY" class="member-name-link"><code>ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Road exit labels are shown with numbers, if available.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#SAFETY_CAMERAS_ALL" class="member-name-link"><code>SAFETY_CAMERAS_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All types of safety cameras are shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#SHADOWS_ALL" class="member-name-link"><code>SHADOWS_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Shadows are shown for extruded buildings and landmarks.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TERRAIN_3D" class="member-name-link"><code>TERRAIN_3D</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Topography-shading is shown on 3d terrain.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TERRAIN_HILLSHADE" class="member-name-link"><code>TERRAIN_HILLSHADE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Topography-shading is shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW" class="member-name-link"><code>TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Only available when Japan map is used.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW" class="member-name-link"><code>TRAFFIC_FLOW_WITH_FREE_FLOW</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic flow shows green lines when there is no traffic congestion.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW" class="member-name-link"><code>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic flow does not show green lines when there is no traffic congestion.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL" class="member-name-link"><code>TRAFFIC_INCIDENTS_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All available traffic incidents are shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_LIGHTS_ALL" class="member-name-link"><code>TRAFFIC_LIGHTS_ALL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All available traffic lights are shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRUCK_PREFERRED_ROADS_ALL" class="member-name-link"><code>TRUCK_PREFERRED_ROADS_ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Display truck preferred roads

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE" class="member-name-link"><code>VEHICLE_RESTRICTIONS_ACTIVE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Inactive time-based restrictions are not shown.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE" class="member-name-link"><code>VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Both active and inactive time-based restrictions are shown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED" class="member-name-link"><code>VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Both active and inactive restrictions are shown, but inactive time-based restrictions are shown as faded.

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

      MapFeatureModes ()

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

  - <div id="sdk-for-android-navigate-DEFAULT" class="section detail">

    ### DEFAULT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT</span>

    </div>

    <div class="block">

    Enables the default mode of a map feature. Can be used with any map feature.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.DEFAULT">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-BUILDING_FOOTPRINTS_ALL" class="section detail">

    ### BUILDING_FOOTPRINTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDING_FOOTPRINTS_ALL</span>

    </div>

    <div class="block">

    All building footprints are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.BUILDING_FOOTPRINTS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-CONGESTION_ZONES_ALL" class="section detail">

    ### CONGESTION_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CONGESTION_ZONES_ALL</span>

    </div>

    <div class="block">

    All congestion zones are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.CONGESTION_ZONES_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-EXTRUDED_BUILDINGS_ALL" class="section detail">

    ### EXTRUDED_BUILDINGS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTRUDED_BUILDINGS_ALL</span>

    </div>

    <div class="block">

    All extruded buildings are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.EXTRUDED_BUILDINGS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-ENVIRONMENTAL_ZONES_ALL" class="section detail">

    ### ENVIRONMENTAL_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ENVIRONMENTAL_ZONES_ALL</span>

    </div>

    <div class="block">

    All environmental zones are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ENVIRONMENTAL_ZONES_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LOW_SPEED_ZONES_ALL" class="section detail">

    ### LOW_SPEED_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LOW_SPEED_ZONES_ALL</span>

    </div>

    <div class="block">

    All low speed zones are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LOW_SPEED_ZONES_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW" class="section detail">

    ### TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</span>

    </div>

    <div class="block">

    Only available when Japan map is used. Traffic flow shows green lines depending on the region. In Japan green lines will not be shown, as if the TRAFFIC_FLOW_WITHOUT_FREE_FLOW were used. In rest of the world, green lines will be shown, as if the TRAFFIC_FLOW_WITH_FREE_FLOW were used.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_FLOW_WITH_FREE_FLOW" class="section detail">

    ### TRAFFIC_FLOW_WITH_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITH_FREE_FLOW</span>

    </div>

    <div class="block">

    Traffic flow shows green lines when there is no traffic congestion.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_FLOW_WITHOUT_FREE_FLOW" class="section detail">

    ### TRAFFIC_FLOW_WITHOUT_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</span>

    </div>

    <div class="block">

    Traffic flow does not show green lines when there is no traffic congestion.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_INCIDENTS_ALL" class="section detail">

    ### TRAFFIC_INCIDENTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_INCIDENTS_ALL</span>

    </div>

    <div class="block">

    All available traffic incidents are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_INCIDENTS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRAFFIC_LIGHTS_ALL" class="section detail">

    ### TRAFFIC_LIGHTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_LIGHTS_ALL</span>

    </div>

    <div class="block">

    All available traffic lights are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_LIGHTS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LANDMARKS_TEXTURED" class="section detail">

    ### LANDMARKS_TEXTURED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LANDMARKS_TEXTURED</span>

    </div>

    <div class="block">

    3D landmarks are textured.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_TEXTURED">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LANDMARKS_GRAYSCALE" class="section detail">

    ### LANDMARKS_GRAYSCALE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LANDMARKS_GRAYSCALE</span>

    </div>

    <div class="block">

    3D landmarks are textured with grayscale filter.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_GRAYSCALE">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-LANDMARKS_TEXTURELESS" class="section detail">

    ### LANDMARKS_TEXTURELESS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LANDMARKS_TEXTURELESS</span>

    </div>

    <div class="block">

    3D landmarks have solid color.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_TEXTURELESS">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE" class="section detail">

    ### VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</span>

    </div>

    <div class="block">

    Both active and inactive time-based restrictions are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED" class="section detail">

    ### VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</span>

    </div>

    <div class="block">

    Both active and inactive restrictions are shown, but inactive time-based restrictions are shown as faded.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-VEHICLE_RESTRICTIONS_ACTIVE" class="section detail">

    ### VEHICLE_RESTRICTIONS_ACTIVE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">VEHICLE_RESTRICTIONS_ACTIVE</span>

    </div>

    <div class="block">

    Inactive time-based restrictions are not shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-SAFETY_CAMERAS_ALL" class="section detail">

    ### SAFETY_CAMERAS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SAFETY_CAMERAS_ALL</span>

    </div>

    <div class="block">

    All types of safety cameras are shown. Includes speed, red light, red light + speed, bus lane, distance and speed section cameras.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.SAFETY_CAMERAS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TERRAIN_HILLSHADE" class="section detail">

    ### TERRAIN_HILLSHADE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TERRAIN_HILLSHADE</span>

    </div>

    <div class="block">

    Topography-shading is shown. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TERRAIN_HILLSHADE">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TERRAIN_3D" class="section detail">

    ### TERRAIN_3D

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TERRAIN_3D</span>

    </div>

    <div class="block">

    Topography-shading is shown on 3d terrain. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TERRAIN_3D">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-PUBLIC_TRANSIT_ALL" class="section detail">

    ### PUBLIC_TRANSIT_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">PUBLIC_TRANSIT_ALL</span>

    </div>

    <div class="block">

    Line geometry for all available public transit systems is shown; including subway, tram, train, monorail, ferry and more. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.PUBLIC_TRANSIT_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-PUBLIC_TRANSIT_ASIA" class="section detail">

    ### PUBLIC_TRANSIT_ASIA

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">PUBLIC_TRANSIT_ASIA</span>

    </div>

    <div class="block">

    Line geometry for selected public transit systems is shown: subway lines in Japan. Only available when Japan map is used. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.PUBLIC_TRANSIT_ASIA">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-ROAD_EXIT_LABELS_NUMBERS_ONLY" class="section detail">

    ### ROAD_EXIT_LABELS_NUMBERS_ONLY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_NUMBERS_ONLY</span>

    </div>

    <div class="block">

    Road exit labels are shown with numbers, if available.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-ROAD_EXIT_LABELS_ALL" class="section detail">

    ### ROAD_EXIT_LABELS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_ALL</span>

    </div>

    <div class="block">

    Road exit labels are shown with numbers and names, if available.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-SHADOWS_ALL" class="section detail">

    ### SHADOWS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SHADOWS_ALL</span>

    </div>

    <div class="block">

    Shadows are shown for extruded buildings and landmarks. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.SHADOWS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-AMBIENT_OCCLUSION_ALL" class="section detail">

    ### AMBIENT_OCCLUSION_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">AMBIENT_OCCLUSION_ALL</span>

    </div>

    <div class="block">

    Ambient occlusion effect is shown for extruded buildings and landmarks. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.AMBIENT_OCCLUSION_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-CONTOURS_ALL" class="section detail">

    ### CONTOURS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTOURS_ALL</span>

    </div>

    <div class="block">

    Contour lines indicating representing elevation changes are shown.

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.CONTOURS_ALL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-navigate-TRUCK_PREFERRED_ROADS_ALL" class="section detail">

    ### TRUCK_PREFERRED_ROADS_ALL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRUCK_PREFERRED_ROADS_ALL</span>

    </div>

    <div class="block">

    Display truck preferred roads

    </div>

    See Also:  
    - <a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRUCK_PREFERRED_ROADS_ALL">Constant Field Values</a>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### MapFeatureModes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapFeatureModes</span>()

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

