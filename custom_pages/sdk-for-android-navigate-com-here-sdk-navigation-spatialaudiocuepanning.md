---
title: "SpatialAudioCuePanning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.SpatialAudioCuePanning → com.here.NativeBase com.here.sdk.navigation.SpatialAudioCuePanning → com.here.sdk.navigation.SpatialAudioCuePanning

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SpatialAudioCuePanning</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Use the SpatialAudioCuePanning to notify each of the azimuths which compose a spatial audio trajectory along the audio cue.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning-spatialazimuthcallback" class="type-name-link" title="interface in com.here.sdk.navigation"><code>SpatialAudioCuePanning.SpatialAzimuthCallback</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Called once startAngularPanning() starts.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      startAngularPanning ( CustomPanningData nextCustomPanningData, SpatialAudioCuePanning.SpatialAzimuthCallback azimuthCallback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.

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

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-startAngularPanning-com-here-sdk-navigation-CustomPanningData-com-here-sdk-navigation-SpatialAudioCuePanning-SpatialAzimuthCallback" class="section detail">

    ### startAngularPanning

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAngularPanning</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation">CustomPanningData</a> nextCustomPanningData, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning-spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a> azimuthCallback)</span>

    </div>

    <div class="block">

    This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer. An optional custom value for CustomPanningData.estimatedAudioCueDuration , CustomPanningData.initialAzimuthInDegrees , or its CustomPanningData.sweepAzimuthInDegrees can be here defined if the default data does not fully match the utilized Language or TTS engine or angle expectations. If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full completion of a previous spatial audio trajectory, then EventTextListener will retrieve the azimuth values of the new maneuver.

    </div>

    Parameters:  
    `nextCustomPanningData` -

    Defines a new set of values related to spatial audio panning. When <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation">`CustomPanningData`</a> is initialized as `null`, the default set of values provided by HERE SDK will be used instead.

    `azimuthCallback` -

    Callback that will signal the next azimuth required to complete a spatial audio trajectory once the angular panning has started. Azimuth angular values are retrieved individually until the full duration of the audio trajectory has been reached, or a new text message has started its angular panning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

