---
title: "AutomotiveCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.AutomotiveCameraBehavior → com.here.NativeBase com.here.sdk.navigation.AutomotiveCameraBehavior → com.here.sdk.navigation.AutomotiveCameraBehavior

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AutomotiveCameraBehavior</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span>

</div>

<div class="block">

Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors. This class acts as a facade, delegating camera operations to either a TrackingCameraBehavior for following the vehicle during navigation or an AreaCameraBehavior for showing overview areas such as points of interest or route previews. The controller supports three states: tracking mode (following the vehicle), area mode (showing geographic regions), or inactive (no automatic camera control). The inactive state allows external control of the camera, such as when responding to user touch events or when UI logic temporarily disables automatic camera behavior. Camera configuration, including animation durations, zoom policies, and maneuver handling settings, can be provided through a JSON configuration string or file. The configuration is validated and parsed during construction. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-activecameratype" class="type-name-link" title="enum class in com.here.sdk.navigation"><code>AutomotiveCameraBehavior.ActiveCameraType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the type of camera currently handling camera updates.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static enum `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-orientationmode" class="type-name-link" title="enum class in com.here.sdk.navigation"><code>AutomotiveCameraBehavior.OrientationMode</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the visual presentation modes for the camera orientation.

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

      AutomotiveCameraBehavior ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class with default camera behaviors and configuration.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      AutomotiveCameraBehavior ( String configJson)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class configured from a JSON string.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-activecameratype" title="enum class in com.here.sdk.navigation">`AutomotiveCameraBehavior.ActiveCameraType`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getActiveCameraType ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the type of camera currently handling camera updates.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-orientationmode" title="enum class in com.here.sdk.navigation">`AutomotiveCameraBehavior.OrientationMode`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOrientationMode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current orientation mode.

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isManeuverDetectionEnabled ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets whether maneuver-based camera adjustments are enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setActiveCameraType ( AutomotiveCameraBehavior.ActiveCameraType value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the type of camera currently handling camera updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setAreaCameraBehaviorGeobox ( GeoBox geobox)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the Area camera to frame the specified geographic bounding box.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setAreaCameraBehaviorVisiblePoints ( List < GeoCoordinates > points,
       boolean includeCurrentPosition)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the Area camera to frame the specified points.

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

  Sets whether maneuver-based camera adjustments are enabled.

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

      setOrientationMode ( AutomotiveCameraBehavior.OrientationMode value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the orientation mode for the tracking camera.

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

  Sets a view rectangle for both child cameras.

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

    ### AutomotiveCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AutomotiveCameraBehavior</span>()

    </div>

    <div class="block">

    Creates a new instance of this class with default camera behaviors and configuration. This constructor automatically creates and configures the underlying TrackingCameraBehavior and AreaCameraBehavior instances with default settings.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String" class="section detail">

    ### AutomotiveCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AutomotiveCameraBehavior</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> configJson)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class configured from a JSON string. The JSON configuration is validated during construction and applied to the underlying TrackingCameraBehavior and AreaCameraBehavior instances.

    </div>

    Parameters:  
    `configJson` -

    A JSON string containing automotive camera configuration settings.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> when the JSON is malformed or contains invalid values.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-setAreaCameraBehaviorVisiblePoints-java-util-List-boolean" class="section detail">

    ### setAreaCameraBehaviorVisiblePoints

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAreaCameraBehaviorVisiblePoints</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\> points, boolean includeCurrentPosition)</span>

    </div>

    <div class="block">

    Configures the Area camera to frame the specified points. The camera calculates the optimal zoom level and center position to display all provided coordinates within the viewport. Use this for showing a single point of interest or multiple points such as safety cameras. This function does not change getActiveCameraType() . To display the configured area view, set getActiveCameraType() to AutomotiveCameraBehavior.ActiveCameraType.AREA . Calling this function overrides any previously set geographic bounding box configured via setAreaCameraBehaviorGeobox(com.here.sdk.core.GeoBox) .

    </div>

    Parameters:  
    `points` -

    The list of geographic coordinates to display.

    `includeCurrentPosition` -

    When true, the current vehicle position is included in the visible area calculation, ensuring the vehicle remains visible alongside the provided points.

    </div>

  - <div id="sdk-for-android-navigate-setAreaCameraBehaviorGeobox-com-here-sdk-core-GeoBox" class="section detail">

    ### setAreaCameraBehaviorGeobox

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAreaCameraBehaviorGeobox</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geobox)</span>

    </div>

    <div class="block">

    Configures the Area camera to frame the specified geographic bounding box. The camera automatically calculates the appropriate zoom level and center position to ensure the entire area is visible within the viewport. This function does not change getActiveCameraType() . To display the configured area view, set getActiveCameraType() to AutomotiveCameraBehavior.ActiveCameraType.AREA . Calling this function overrides any previously set visible points configured via setAreaCameraBehaviorVisiblePoints(java.util.List\<com.here.sdk.core.GeoCoordinates\>, boolean) .

    </div>

    Parameters:  
    `geobox` -

    The geographic bounding box to display.

    </div>

  - <div id="sdk-for-android-navigate-isManeuverDetectionEnabled" class="section detail">

    ### isManeuverDetectionEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverDetectionEnabled</span>()

    </div>

    <div class="block">

    Gets whether maneuver-based camera adjustments are enabled. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration. If tracking is currently active when this property is changed, the setting takes effect immediately. Otherwise, it will apply the next time tracking is activated. The initial state is determined by the camera configuration provided during construction.

    </div>

    Returns:  
    Enables or disables automatic camera adjustments during upcoming maneuvers.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverDetectionEnabled-boolean" class="section detail">

    ### setManeuverDetectionEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverDetectionEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether maneuver-based camera adjustments are enabled. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration. If tracking is currently active when this property is changed, the setting takes effect immediately. Otherwise, it will apply the next time tracking is activated. The initial state is determined by the camera configuration provided during construction.

    </div>

    Parameters:  
    `value` -

    Enables or disables automatic camera adjustments during upcoming maneuvers.

    </div>

  - <div id="sdk-for-android-navigate-getViewRectangle" class="section detail">

    ### getViewRectangle

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span class="element-name">getViewRectangle</span>()

    </div>

    <div class="block">

    Gets the current view rectangle, if it's set. Defines a sub-space of the screen that the behavior should consider for camera updates. This property is forwarded to both the tracking and area cameras, ensuring consistent viewport constraints across all camera modes. If not set, it uses the viewport bounds of the underlying map view.

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

    Sets a view rectangle for both child cameras. Defines a sub-space of the screen that the behavior should consider for camera updates. This property is forwarded to both the tracking and area cameras, ensuring consistent viewport constraints across all camera modes. If not set, it uses the viewport bounds of the underlying map view.

    </div>

    Parameters:  
    `value` -

    The view rectangle for camera updates.

    </div>

  - <div id="sdk-for-android-navigate-getActiveCameraType" class="section detail">

    ### getActiveCameraType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a></span> <span class="element-name">getActiveCameraType</span>()

    </div>

    <div class="block">

    Gets the type of camera currently handling camera updates. Defines which camera behavior is currently active: AutomotiveCameraBehavior.ActiveCameraType.NONE (free navigation), AutomotiveCameraBehavior.ActiveCameraType.TRACKING , or AutomotiveCameraBehavior.ActiveCameraType.AREA .

    </div>

    Returns:  
    The active camera type.

    </div>

  - <div id="sdk-for-android-navigate-setActiveCameraType-com-here-sdk-navigation-AutomotiveCameraBehavior-ActiveCameraType" class="section detail">

    ### setActiveCameraType

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveCameraType</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a> value)</span>

    </div>

    <div class="block">

    Sets the type of camera currently handling camera updates. If AutomotiveCameraBehavior.ActiveCameraType.AREA is selected, the most recently configured area framing is used. If AutomotiveCameraBehavior.ActiveCameraType.TRACKING is selected, the tracking camera behavior is used. To deactivate set to AutomotiveCameraBehavior.ActiveCameraType.NONE . Defines which camera behavior is currently active: AutomotiveCameraBehavior.ActiveCameraType.NONE (free navigation), AutomotiveCameraBehavior.ActiveCameraType.TRACKING , or AutomotiveCameraBehavior.ActiveCameraType.AREA .

    </div>

    Parameters:  
    `value` -

    The active camera type.

    </div>

  - <div id="sdk-for-android-navigate-getOrientationMode" class="section detail">

    ### getOrientationMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a></span> <span class="element-name">getOrientationMode</span>()

    </div>

    <div class="block">

    Gets the current orientation mode. Defines the camera's viewing angle and orientation for tracking mode. In AutomotiveCameraBehavior.OrientationMode.MODE_2D , the camera looks straight down and rotates with the vehicle heading. In AutomotiveCameraBehavior.OrientationMode.MODE_3D , the camera is tilted for a perspective view. In AutomotiveCameraBehavior.OrientationMode.MODE_NORTH_UP , the camera maintains north-up orientation regardless of vehicle heading. Changes to this property take effect immediately on the tracking camera and are preserved when switching between tracking and area modes.

    </div>

    Returns:  
    The current orientation mode of the camera.

    </div>

  - <div id="sdk-for-android-navigate-setOrientationMode-com-here-sdk-navigation-AutomotiveCameraBehavior-OrientationMode" class="section detail">

    ### setOrientationMode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientationMode</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior-orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a> value)</span>

    </div>

    <div class="block">

    Sets the orientation mode for the tracking camera. Defines the camera's viewing angle and orientation for tracking mode. In AutomotiveCameraBehavior.OrientationMode.MODE_2D , the camera looks straight down and rotates with the vehicle heading. In AutomotiveCameraBehavior.OrientationMode.MODE_3D , the camera is tilted for a perspective view. In AutomotiveCameraBehavior.OrientationMode.MODE_NORTH_UP , the camera maintains north-up orientation regardless of vehicle heading. Changes to this property take effect immediately on the tracking camera and are preserved when switching between tracking and area modes.

    </div>

    Parameters:  
    `value` -

    The current orientation mode of the camera.

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

