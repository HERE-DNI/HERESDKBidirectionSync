---
title: "MapCameraLimits (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapCameraLimits → com.here.NativeBase com.here.sdk.mapview.MapCameraLimits → com.here.sdk.mapview.MapCameraLimits

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraLimits</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Controls constraints on map camera parameters. When constraints are set, they are enforced for current camera state and for all future changes to the camera. When setting, limits are applied on next rendering loop.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  `static final double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits#MAX_TILT" class="member-name-link"><code>MAX_TILT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Absolute maximum possible value of tilt angle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits#MAX_ZOOM_LEVEL" class="member-name-link"><code>MAX_ZOOM_LEVEL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Absolute maximum possible value of zoom level.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits#MIN_TILT" class="member-name-link"><code>MIN_TILT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Absolute minimum possible value of tilt angle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL" class="member-name-link"><code>MIN_ZOOM_LEVEL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Absolute minimum possible value of zoom level.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      clearBearingRanges ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Clears bearing ranges for all zoom values and resets bearing range to default.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      clearTiltRanges ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Clears tilt ranges for all zoom values and resets tilt range to default.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`AngleRange`](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBearingRange ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set bearing range.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTargetArea ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a GeoBox that limits the camera target to a specific geographical area.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`AngleRange`](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTiltRange ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current tilt range.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureRange`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getZoomRange ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set camera zoom range.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBearingRange ( AngleRange value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a new bearing range.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBearingRangeAtZoom ( MapMeasure zoom, AngleRange bearingRange)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the bearing range within which the camera can rotate at a given zoom.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTargetArea ( GeoBox value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a GeoBox that limits the camera target to a specific geographical area.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTiltRange ( AngleRange value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a new tilt limit range.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTiltRangeAtZoom ( MapMeasure zoom, AngleRange tiltRange)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets tilt ranges that can be set on the camera at given zoom.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setZoomRange ( MapMeasureRange value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a new camera zoom range.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-MIN_TILT" class="section detail">

    ### MIN_TILT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MIN_TILT</span>

    </div>

    <div class="block">

    Absolute minimum possible value of tilt angle.

    </div>

    See Also:  
    - [Constant Field Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_TILT)

    </div>

  - <div id="sdk-for-android-explore-MAX_TILT" class="section detail">

    ### MAX_TILT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MAX_TILT</span>

    </div>

    <div class="block">

    Absolute maximum possible value of tilt angle.

    </div>

    See Also:  
    - [Constant Field Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_TILT)

    </div>

  - <div id="sdk-for-android-explore-MIN_ZOOM_LEVEL" class="section detail">

    ### MIN_ZOOM_LEVEL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MIN_ZOOM_LEVEL</span>

    </div>

    <div class="block">

    Absolute minimum possible value of zoom level.

    </div>

    See Also:  
    - [Constant Field Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_ZOOM_LEVEL)

    </div>

  - <div id="sdk-for-android-explore-MAX_ZOOM_LEVEL" class="section detail">

    ### MAX_ZOOM_LEVEL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MAX_ZOOM_LEVEL</span>

    </div>

    <div class="block">

    Absolute maximum possible value of zoom level.

    </div>

    See Also:  
    - [Constant Field Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_ZOOM_LEVEL)

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-setBearingRangeAtZoom-com-here-sdk-mapview-MapMeasure-com-here-sdk-core-AngleRange" class="section detail">

    ### setBearingRangeAtZoom

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingRangeAtZoom</span><wbr></wbr><span class="parameters">(@NonNull [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") zoom, @NonNull [AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core") bearingRange)</span>

    </div>

    <div class="block">

    Sets the bearing range within which the camera can rotate at a given zoom. The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no bearing range is specified for MIN_ZOOM_LEVEL , the bearing range set through setBearingRange(com.here.sdk.core.AngleRange) is used for interpolation. Zoom values outside the supported zoom range are ignored. By default, the maximum bearing range for all zoom values is set during initialization.

    </div>

    Parameters:  
    `zoom` -

    Zoom at which the range is set.

    `bearingRange` -

    Bearing range.

    </div>

  - <div id="sdk-for-android-explore-clearBearingRanges" class="section detail">

    ### clearBearingRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearBearingRanges</span>()

    </div>

    <div class="block">

    Clears bearing ranges for all zoom values and resets bearing range to default.

    </div>

    </div>

  - <div id="sdk-for-android-explore-setTiltRangeAtZoom-com-here-sdk-mapview-MapMeasure-com-here-sdk-core-AngleRange" class="section detail">

    ### setTiltRangeAtZoom

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltRangeAtZoom</span><wbr></wbr><span class="parameters">(@NonNull [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") zoom, @NonNull [AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core") tiltRange)</span>

    </div>

    <div class="block">

    Sets tilt ranges that can be set on the camera at given zoom. The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no tilt range is specified for MIN_ZOOM_LEVEL , the tilt range set through setTiltRange(com.here.sdk.core.AngleRange) is used for interpolation. Zoom or tilt values outside the supported zoom and tilt range are ignored. By default, the maximum tilt range for all zoom values is set during initialization.

    </div>

    Parameters:  
    `zoom` -

    Zoom at which the range is set.

    `tiltRange` -

    Tilt range.

    </div>

  - <div id="sdk-for-android-explore-clearTiltRanges" class="section detail">

    ### clearTiltRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTiltRanges</span>()

    </div>

    <div class="block">

    Clears tilt ranges for all zoom values and resets tilt range to default.

    </div>

    </div>

  - <div id="sdk-for-android-explore-getTiltRange" class="section detail">

    ### getTiltRange

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")</span> <span class="element-name">getTiltRange</span>()

    </div>

    <div class="block">

    Gets the current tilt range. By default, a MIN_TILT - MAX_TILT tilt range is set during initialization. This range might not be yet active if no rendering loop has been executed since the last call to set the range.

    </div>

    Returns:  
    The tilt range that can be applied to the camera.

    </div>

  - <div id="sdk-for-android-explore-setTiltRange-com-here-sdk-core-AngleRange" class="section detail">

    ### setTiltRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltRange</span><wbr></wbr><span class="parameters">(@NonNull [AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets a new tilt limit range. The supported values fall inside MIN_TILT - MAX_TILT range. Values outside the supported range are ignored. If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum, depending on which is closest. This new limit range becomes active during the next rendering loop. All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.

    </div>

    Parameters:  
    `value` -

    The tilt range that can be applied to the camera.

    </div>

  - <div id="sdk-for-android-explore-getBearingRange" class="section detail">

    ### getBearingRange

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")</span> <span class="element-name">getBearingRange</span>()

    </div>

    <div class="block">

    Gets the currently set bearing range. This may not be active now if no rendering loop has been executed since the last call to set the range. By default, range for a full circle is set during initialization.

    </div>

    Returns:  
    The bearing range within which the camera can be rotated.

    </div>

  - <div id="sdk-for-android-explore-setBearingRange-com-here-sdk-core-AngleRange" class="section detail">

    ### setBearingRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingRange</span><wbr></wbr><span class="parameters">(@NonNull [AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets a new bearing range. It will be updated during the next rendering loop. All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values. If the current camera bearing exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

    </div>

    Parameters:  
    `value` -

    The bearing range within which the camera can be rotated.

    </div>

  - <div id="sdk-for-android-explore-getZoomRange" class="section detail">

    ### getZoomRange

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")</span> <span class="element-name">getZoomRange</span>()

    </div>

    <div class="block">

    Gets the currently set camera zoom range. By default, a MIN_ZOOM_LEVEL - MAX_ZOOM_LEVEL zoom range is set during initialization.

    </div>

    Returns:  
    The zoom range that can be applied to the camera.

    </div>

  - <div id="sdk-for-android-explore-setZoomRange-com-here-sdk-mapview-MapMeasureRange" class="section detail">

    ### setZoomRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomRange</span><wbr></wbr><span class="parameters">(@NonNull [MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets a new camera zoom range. The supported values fall inside MIN_ZOOM_LEVEL - MAX_ZOOM_LEVEL range. Values outside the supported zoom range are ignored. If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest. This new limit range becomes active during the next rendering loop.

    </div>

    Parameters:  
    `value` -

    The zoom range that can be applied to the camera.

    </div>

  - <div id="sdk-for-android-explore-getTargetArea" class="section detail">

    ### getTargetArea

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">getTargetArea</span>()

    </div>

    <div class="block">

    Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.

    </div>

    Returns:  
    Geographical area to which the camera target is limited.

    </div>

  - <div id="sdk-for-android-explore-setTargetArea-com-here-sdk-core-GeoBox" class="section detail">

    ### setTargetArea

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetArea</span><wbr></wbr><span class="parameters">(@Nullable [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets a GeoBox that limits the camera target to a specific geographical area. Set to null to remove the limit.

    </div>

    Parameters:  
    `value` -

    Geographical area to which the camera target is limited.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

