---
title: "TrackingCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.TrackingCameraBehavior → com.here.NativeBase com.here.sdk.navigation.TrackingCameraBehavior → com.here.sdk.navigation.TrackingCameraBehavior

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TrackingCameraBehavior</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span>

</div>

<div class="block">

Use this class to follow a moving target. The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target. Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

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

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Configuration for mapping functional road classes to zoom levels.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Configuration that defines how TrackingCameraBehavior reacts to nearby maneuvers.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRule</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines a single rule that determines how TrackingCameraBehavior reacts to nearby maneuvers when the current position matches this rule.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRuleOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines a set of configurations specific to a TrackingCameraBehavior.ManeuverRule .

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverzoomrange" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverZoomRange</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the bounds within which the zoom level is constrained when approaching a maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Configuration for computing zoom levels from speed thresholds defined per road classification.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedThreshold</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines a zoom level triggered when the vehicle reaches a specific speed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" class="type-name-link" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ZoomPolicy</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines zoom behavior in different policy settings.

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

      TrackingCameraBehavior ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      defaultFunctionalRoadClassZoomPolicyOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ManeuverModeConfiguration`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      defaultManeuverModeConfiguration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.SpeedBasedZoomPolicyOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      defaultSpeedBasedZoomPolicyOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      flagFixedDurationForNextAnimation ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Enables fixed-duration animation mode for the next property change.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBearingInDegrees ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the bearing in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ManeuverModeConfiguration`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverModeConfiguration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current maneuver mode configuration, or null if not set.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMaxRotationSpeedInDegreesPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maximum rotation speed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">`Anchor2D`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNormalizedPrincipalPoint ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPrincipalPointAnimationDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current principal point animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRecenterAnimationDuration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the recenter animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTiltInDegrees ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the camera tilt in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">`Rectangle2D`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewRectangle ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current view rectangle, if it's set.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ZoomPolicy`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getZoomPolicy ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current zoom computation strategy.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getZoomSpeedInLevelsPerSecond ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the zoom level transition speed.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isManeuverDetectionEnabled ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets whether maneuver detection is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBearingInDegrees ( Double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the bearing in degrees.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverDetectionEnabled (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether maneuver detection is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverModeConfiguration ( TrackingCameraBehavior.ManeuverModeConfiguration maneuverModeConfiguration)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the configuration for camera behavior near maneuvers.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMaxRotationSpeedInDegreesPerSecond (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the maximum rotation speed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setNormalizedPrincipalPoint ( Anchor2D value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a normalized principal point to be used during navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPrincipalPointAnimationDuration ( Duration value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current principal point animation in milliseconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRecenterAnimationDuration ( Duration value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the recenter animation duration in milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTiltInDegrees (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the camera tilt in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setViewRectangle ( Rectangle2D value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a view rectangle.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setZoomPolicy ( TrackingCameraBehavior.ZoomPolicy value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current zoom computation strategy.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setZoomSpeedInLevelsPerSecond (double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the zoom level transition speed.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### TrackingCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrackingCameraBehavior</span>()

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-flagFixedDurationForNextAnimation" class="section detail">

    ### flagFixedDurationForNextAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flagFixedDurationForNextAnimation</span>()

    </div>

    <div class="block">

    Enables fixed-duration animation mode for the next property change. When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees) will animate using a fast fixed-duration animation instead of the default speed-based animation. The flag is automatically reset after the next setter is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-setManeuverModeConfiguration-com-here-sdk-navigation-TrackingCameraBehavior-ManeuverModeConfiguration" class="section detail">

    ### setManeuverModeConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverModeConfiguration</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a> maneuverModeConfiguration)</span>

    </div>

    <div class="block">

    Sets the configuration for camera behavior near maneuvers. Defines how the camera reacts to nearby maneuvers when isManeuverDetectionEnabled() is true . When set to null , the camera does not react to maneuvers. The configuration must contain at least one rule to be valid. Defaults to null .

    </div>

    Parameters:  
    `maneuverModeConfiguration` -

    The maneuver mode configuration. Invalid configurations are rejected.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverModeConfiguration" class="section detail">

    ### getManeuverModeConfiguration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span class="element-name">getManeuverModeConfiguration</span>()

    </div>

    <div class="block">

    Gets the current maneuver mode configuration, or null if not set.

    </div>

    Returns:  
    The current maneuver mode configuration.

    </div>

  - <div id="sdk-for-android-navigate-defaultFunctionalRoadClassZoomPolicyOptions" class="section detail">

    ### defaultFunctionalRoadClassZoomPolicyOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></span> <span class="element-name">defaultFunctionalRoadClassZoomPolicyOptions</span>()

    </div>

    Returns:  
    The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions`</a>.

    </div>

  - <div id="sdk-for-android-navigate-defaultSpeedBasedZoomPolicyOptions" class="section detail">

    ### defaultSpeedBasedZoomPolicyOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></span> <span class="element-name">defaultSpeedBasedZoomPolicyOptions</span>()

    </div>

    Returns:  
    The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.SpeedBasedZoomPolicyOptions`</a>.

    </div>

  - <div id="sdk-for-android-navigate-defaultManeuverModeConfiguration" class="section detail">

    ### defaultManeuverModeConfiguration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span class="element-name">defaultManeuverModeConfiguration</span>()

    </div>

    Returns:  
    The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">`TrackingCameraBehavior.ManeuverModeConfiguration`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getRecenterAnimationDuration" class="section detail">

    ### getRecenterAnimationDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getRecenterAnimationDuration</span>()

    </div>

    <div class="block">

    Gets the recenter animation duration in milliseconds. Time to recenter the camera reaching current car position. Defaults to 500 milliseconds, or half a second.

    </div>

    Returns:  
    The duration of recenter animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-setRecenterAnimationDuration-com-here-time-Duration" class="section detail">

    ### setRecenterAnimationDuration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecenterAnimationDuration</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span>

    </div>

    <div class="block">

    Sets the recenter animation duration in milliseconds. Time to recenter the camera reaching current car position. Defaults to 500 milliseconds, or half a second.

    </div>

    Parameters:  
    `value` -

    The duration of recenter animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-getViewRectangle" class="section detail">

    ### getViewRectangle

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span class="element-name">getViewRectangle</span>()

    </div>

    <div class="block">

    Gets the current view rectangle, if it's set. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to null . If not set, it uses the viewport bounds of the underlying map view.

    </div>

    Returns:  
    The view rectangle for camera updates.

    </div>

  - <div id="sdk-for-android-navigate-setViewRectangle-com-here-sdk-core-Rectangle2D" class="section detail">

    ### setViewRectangle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewRectangle</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</span>

    </div>

    <div class="block">

    Sets a view rectangle. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to null . If not set, it uses the viewport bounds of the underlying map view.

    </div>

    Parameters:  
    `value` -

    The view rectangle for camera updates.

    </div>

  - <div id="sdk-for-android-navigate-getPrincipalPointAnimationDuration" class="section detail">

    ### getPrincipalPointAnimationDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getPrincipalPointAnimationDuration</span>()

    </div>

    <div class="block">

    Gets the current principal point animation duration in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

    </div>

    Returns:  
    The duration of principal point animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-setPrincipalPointAnimationDuration-com-here-time-Duration" class="section detail">

    ### setPrincipalPointAnimationDuration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrincipalPointAnimationDuration</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span>

    </div>

    <div class="block">

    Sets the current principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

    </div>

    Parameters:  
    `value` -

    The duration of principal point animation in milliseconds.

    </div>

  - <div id="sdk-for-android-navigate-getTiltInDegrees" class="section detail">

    ### getTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTiltInDegrees</span>()

    </div>

    <div class="block">

    Gets the camera tilt in degrees. Camera tilt angle relative to the ground plane, in degrees. Defaults to 50.

    </div>

    Returns:  
    The value of camera tilt in degrees.

    </div>

  - <div id="sdk-for-android-navigate-setTiltInDegrees-double" class="section detail">

    ### setTiltInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltInDegrees</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the camera tilt in degrees. Camera tilt angle relative to the ground plane, in degrees. Defaults to 50.

    </div>

    Parameters:  
    `value` -

    The value of camera tilt in degrees.

    </div>

  - <div id="sdk-for-android-navigate-getBearingInDegrees" class="section detail">

    ### getBearingInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getBearingInDegrees</span>()

    </div>

    <div class="block">

    Gets the bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to null , which means the camera derives the bearing from the Location , so that it points to the direction of travel. If this property is null and the device does not provide bearing, the last known value is used or zero otherwise.

    </div>

    Returns:  
    The camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-setBearingInDegrees-java-lang-Double" class="section detail">

    ### setBearingInDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingInDegrees</span><wbr></wbr><span class="parameters">(@Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> value)</span>

    </div>

    <div class="block">

    Sets the bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to null , which means the camera derives the bearing from the Location , so that it points to the direction of travel. If this property is null and the device does not provide bearing, the last known value is used or zero otherwise.

    </div>

    Parameters:  
    `value` -

    The camera bearing in degrees.

    </div>

  - <div id="sdk-for-android-navigate-getMaxRotationSpeedInDegreesPerSecond" class="section detail">

    ### getMaxRotationSpeedInDegreesPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getMaxRotationSpeedInDegreesPerSecond</span>()

    </div>

    <div class="block">

    Gets the maximum rotation speed. Maximum bearing rotation speed in degrees per second, limiting how fast the camera turns. Defaults to 20 degrees per second.

    </div>

    Returns:  
    The maximum rotation speed.

    </div>

  - <div id="sdk-for-android-navigate-setMaxRotationSpeedInDegreesPerSecond-double" class="section detail">

    ### setMaxRotationSpeedInDegreesPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaxRotationSpeedInDegreesPerSecond</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the maximum rotation speed. Maximum bearing rotation speed in degrees per second, limiting how fast the camera turns. Defaults to 20 degrees per second.

    </div>

    Parameters:  
    `value` -

    The maximum rotation speed.

    </div>

  - <div id="sdk-for-android-navigate-getZoomSpeedInLevelsPerSecond" class="section detail">

    ### getZoomSpeedInLevelsPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getZoomSpeedInLevelsPerSecond</span>()

    </div>

    <div class="block">

    Gets the zoom level transition speed. Speed factor controlling how quickly the camera transitions between zoom levels Defaults to 0.5 zoom levels per second.

    </div>

    Returns:  
    The zoom level transition speed.

    </div>

  - <div id="sdk-for-android-navigate-setZoomSpeedInLevelsPerSecond-double" class="section detail">

    ### setZoomSpeedInLevelsPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomSpeedInLevelsPerSecond</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the zoom level transition speed. Speed factor controlling how quickly the camera transitions between zoom levels Defaults to 0.5 zoom levels per second.

    </div>

    Parameters:  
    `value` -

    The zoom level transition speed.

    </div>

  - <div id="sdk-for-android-navigate-getZoomPolicy" class="section detail">

    ### getZoomPolicy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">getZoomPolicy</span>()

    </div>

    <div class="block">

    Gets the current zoom computation strategy. Defines the strategy used to compute the zoom level based on scene heuristics. Defaults to a fixed zoom policy at zoom level 16.5.

    </div>

    Returns:  
    The strategy of computing the zoom level.

    </div>

  - <div id="sdk-for-android-navigate-setZoomPolicy-com-here-sdk-navigation-TrackingCameraBehavior-ZoomPolicy" class="section detail">

    ### setZoomPolicy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomPolicy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a> value)</span>

    </div>

    <div class="block">

    Sets the current zoom computation strategy. Defines the strategy used to compute the zoom level based on scene heuristics. Defaults to a fixed zoom policy at zoom level 16.5.

    </div>

    Parameters:  
    `value` -

    The strategy of computing the zoom level.

    </div>

  - <div id="sdk-for-android-navigate-isManeuverDetectionEnabled" class="section detail">

    ### isManeuverDetectionEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverDetectionEnabled</span>()

    </div>

    <div class="block">

    Gets whether maneuver detection is enabled. When true , the camera detects adjacent maneuvers and reacts according to the TrackingCameraBehavior.ManeuverModeConfiguration set via setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration) . A valid TrackingCameraBehavior.ManeuverModeConfiguration must be set for the camera to react. Defaults to false .

    </div>

    Returns:  
    Whether maneuver detection is enabled.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverDetectionEnabled-boolean" class="section detail">

    ### setManeuverDetectionEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverDetectionEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether maneuver detection is enabled. When true , the camera detects adjacent maneuvers and reacts according to the TrackingCameraBehavior.ManeuverModeConfiguration set via setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration) . A valid TrackingCameraBehavior.ManeuverModeConfiguration must be set for the camera to react. Defaults to false .

    </div>

    Parameters:  
    `value` -

    Whether maneuver detection is enabled.

    </div>

  - <div id="sdk-for-android-navigate-getNormalizedPrincipalPoint" class="section detail">

    ### getNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()

    </div>

    <div class="block">

    Gets the currently set normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior#getNormalizedPrincipalPoint(">`getNormalizedPrincipalPoint`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

    Returns:  
    The normalized principal point.

    </div>

  - <div id="sdk-for-android-navigate-setNormalizedPrincipalPoint-com-here-sdk-core-Anchor2D" class="section detail">

    ### setNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span>

    </div>

    <div class="block">

    Sets a normalized principal point to be used during navigation. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D">`setNormalizedPrincipalPoint`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

    Parameters:  
    `value` -

    The normalized principal point.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

