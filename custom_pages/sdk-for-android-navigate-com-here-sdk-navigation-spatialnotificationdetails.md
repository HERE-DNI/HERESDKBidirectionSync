---
title: "SpatialNotificationDetails (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.SpatialNotificationDetails → com.here.sdk.navigation.SpatialNotificationDetails

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SpatialNotificationDetails</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">`SpatialAudioCuePanning`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#audioCuePanning" class="member-name-link"><code>audioCuePanning</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Object to start the angular panning when spatialization of the text notification is desired

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#estimatedAudioCueDuration" class="member-name-link"><code>estimatedAudioCueDuration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Estimation of the required time to play an audio cue at speech rate 1.0.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#initialAzimuthInDegrees" class="member-name-link"><code>initialAzimuthInDegrees</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Initial desired angular position of the upcoming audio cue.

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

      SpatialNotificationDetails (double initialAzimuthInDegrees, SpatialAudioCuePanning audioCuePanning, Duration estimatedAudioCueDuration)

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

  - <div id="sdk-for-android-navigate-initialAzimuthInDegrees" class="section detail">

    ### initialAzimuthInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">initialAzimuthInDegrees</span>

    </div>

    <div class="block">

    Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" ( ManeuverAction.RightTurn ) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps". The orientation in space for initialAzimuthInDegrees can be represented by the following angular values: Front Right Rear Left 0° +90° +- 180 -90°

    </div>

    </div>

  - <div id="sdk-for-android-navigate-audioCuePanning" class="section detail">

    ### audioCuePanning

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a></span> <span class="element-name">audioCuePanning</span>

    </div>

    <div class="block">

    Object to start the angular panning when spatialization of the text notification is desired

    </div>

    </div>

  - <div id="sdk-for-android-navigate-estimatedAudioCueDuration" class="section detail">

    ### estimatedAudioCueDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">estimatedAudioCueDuration</span>

    </div>

    <div class="block">

    Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-com-here-sdk-navigation-SpatialAudioCuePanning-com-here-time-Duration" class="section detail">

    ### SpatialNotificationDetails

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SpatialNotificationDetails</span><wbr></wbr><span class="parameters">(double initialAzimuthInDegrees, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation">SpatialAudioCuePanning</a> audioCuePanning, @NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> estimatedAudioCueDuration)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `initialAzimuthInDegrees` -

    Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as "Turn right on" (`ManeuverAction.RightTurn`) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left") and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio "jumps". The orientation in space for <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails#initialAzimuthInDegrees">`initialAzimuthInDegrees`</a> can be represented by the following angular values:

    | Front | Right |  Rear  | Left |
    |:-----:|:-----:|:------:|:----:|
    |  0°   | +90°  | +- 180 | -90° |

    </p>

    `audioCuePanning` -

    Object to start the angular panning when spatialization of the text notification is desired

    `estimatedAudioCueDuration` -

    Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

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

