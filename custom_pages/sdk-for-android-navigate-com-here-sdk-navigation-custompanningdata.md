---
title: "CustomPanningData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.CustomPanningData → com.here.sdk.navigation.CustomPanningData

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">CustomPanningData</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications. The orientation in space for initialAzimuthInDegrees and sweepAzimuthInDegrees can be represented by the following angular values: Front Right Rear Left 0° +90° +- 180 -90° When any of the members of CustomPanningData are initialized as null, the default value provided by HERE SDK will be used instead. The audio cue is spatialized considering the action of both maneuvers, for example, the audio cue 'Now turn right and then turn left' will be spatialized as following: 'Now turn right' will be heard as coming from the right. 'and then turn left' will be heard as coming from the left. Note: The estimation for playing both audio cues could be not fully accurate and therefore a mismatch between the audio source and the audio cue message could be perceived.

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

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#estimatedAudioCueDuration" class="member-name-link"><code>estimatedAudioCueDuration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Customized estimated duration for playing the audio cue on the selected TTS Engine.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#initialAzimuthInDegrees" class="member-name-link"><code>initialAzimuthInDegrees</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Initial desired angular position of the upcoming audio cue.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata#sweepAzimuthInDegrees" class="member-name-link"><code>sweepAzimuthInDegrees</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Sweep angle of the upcoming audio cue.

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

      CustomPanningData ( Duration estimatedAudioCueDuration, Double initialAzimuthInDegrees, Double sweepAzimuthInDegrees)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-estimatedAudioCueDuration" class="section detail">

    ### estimatedAudioCueDuration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">estimatedAudioCueDuration</span>

    </div>

    <div class="block">

    Customized estimated duration for playing the audio cue on the selected TTS Engine. When not used, HERE SDK's estimation will be used instead.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-initialAzimuthInDegrees" class="section detail">

    ### initialAzimuthInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">initialAzimuthInDegrees</span>

    </div>

    <div class="block">

    Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" ( ManeuverAction.RightTurn ) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps".

    </div>

    </div>

  - <div id="sdk-for-android-navigate-sweepAzimuthInDegrees" class="section detail">

    ### sweepAzimuthInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">sweepAzimuthInDegrees</span>

    </div>

    <div class="block">

    Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (i.e. ManeuverAction.RightTurn ), within an initial_azimuth_in_degrees of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. ManeuverAction.LeftTurn ), the initial_azimuth_in_degrees could be set to +5 degrees and the sweep_azimuth_in_degrees to -95 degrees

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-time-Duration-java-lang-Double-java-lang-Double" class="section detail">

    ### CustomPanningData

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CustomPanningData</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> initialAzimuthInDegrees, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> sweepAzimuthInDegrees)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `estimatedAudioCueDuration` -

    Customized estimated duration for playing the audio cue on the selected TTS Engine. When not used, HERE SDK's estimation will be used instead.

    `initialAzimuthInDegrees` -

    Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps".

    `sweepAzimuthInDegrees` -

    Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (i.e. `ManeuverAction.RightTurn`), within an `initial_azimuth_in_degrees` of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. `ManeuverAction.LeftTurn`), the `initial_azimuth_in_degrees` could be set to +5 degrees and the `sweep_azimuth_in_degrees` to -95 degrees

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

