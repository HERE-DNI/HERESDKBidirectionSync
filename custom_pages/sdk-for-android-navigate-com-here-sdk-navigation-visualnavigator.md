---
title: "VisualNavigator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.VisualNavigator → com.here.NativeBase com.here.sdk.navigation.VisualNavigator → com.here.sdk.navigation.VisualNavigator

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VisualNavigator</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></span>

</div>

<div class="block">

This class provides all functionality of NavigatorInterface . In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to Navigator , this class continuously reacts to new locations provided from a location source and acts as a LocationListener . Note that the VisualNavigator takes control of the MapView's (maximum) frame rate when rendering, i.e., between startRendering(com.here.sdk.mapview.MapViewBase) and stopRendering() calls. It overwrites the MapView's frame rate when some camera behavior is set using the getGuidanceFrameRate() . When no camera behavior is preset, the original MapView's frame rate (the value prior to the startRendering(com.here.sdk.mapview.MapViewBase) call) will be used. While the VisualNavigator is rendering, direct changes in the MapView's frame rate can lead to unexpected behavior and therefore should be avoided.

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

      VisualNavigator ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      VisualNavigator ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      VisualNavigator ( SDKNativeEngine sdkEngine, NavigatorInterface navigator)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class using provided instance of NavigatorInterface as source of data.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      VisualNavigator ( NavigatorInterface navigator)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class using provided instance of NavigatorInterface as source of data.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateRemainingDistanceInMeters ( GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This method calculates the distance between the current position and given coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      defaultRouteManeuverArrowMeasureDependentWidths ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Retrieves a dictionary of default route and maneuver arrow widths as a function of MapMeasure s.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">`LanguageCode`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getAvailableLanguagesForManeuverNotifications ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the list of languages for maneuver notification currently available in the SDK.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBorderCrossingWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about border crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">`BorderCrossingWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBorderCrossingWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets border crossing warning options to be passed to BorderCrossingWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">`CameraBehavior`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCameraBehavior ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set camera behavior.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">`VisualNavigatorColors`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getColors ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets an object containing colors used to render route progress and maneuver arrow visualization.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">`CurrentSituationLaneAssistanceViewListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCurrentSituationLaneAssistanceViewListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive current situation lane assistance view notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">`LocationIndicator`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCustomLocationIndicator ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently set LocationIndicator .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">`DangerZoneWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDangerZoneWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive current danger zones notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDebugGpxFilePath ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the path of the GPX file, is any available, currently being displayed on the map.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">`DestinationReachedListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDestinationReachedListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notify when the destination has been reached.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">`EnvironmentalZoneWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEnvironmentalZoneWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive current environmental zones notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">`EventTextListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEventTextListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies when a text notification is available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">`EventTextOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEventTextOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text notification options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGuidanceFrameRate ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frame rate used during guidance.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">`InterpolatedLocationListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInterpolatedLocationListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that receives interpolated locations.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">`JunctionViewLaneAssistanceListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getJunctionViewLaneAssistanceListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive junction view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">`LocationManager`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLocationManager ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the location manager instance used by the navigator.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">`LowSpeedZoneWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLowSpeedZoneWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about low speed zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">`Maneuver`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuver (int index)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns maneuver at the given index.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverArrowWidthFactor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the factor that multiplies width of the maneuver arrow defined by getMeasureDependentWidth() .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverNotificationOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maneuver notification options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationTimingOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverNotificationTimingOptions ( TransportMode transportMode, TimingProfile timingProfile)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">`ManeuverViewLaneAssistanceListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverViewLaneAssistanceListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive maneuver view lane assistance notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMeasureDependentWidth ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the MapMeasure dependent polyline and maneuver arrow width in pixels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">`MilestoneStatusListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMilestoneStatusListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies when a Milestone has been reached or missed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">`NavigableLocationListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNavigableLocationListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies current location updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">`OffRoadDestinationReachedListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOffRoadDestinationReachedListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies when the off-road destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">`OffRoadProgressListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOffRoadProgressListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies about off-road progress.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">`PostActionListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPostActionListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive post action notifications, such as a charge action at a charging station.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">`RailwayCrossingWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRailwayCrossingWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about railway crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">`RealisticViewWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRealisticViewWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about junction views on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">`RealisticViewWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRealisticViewWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">`RoadAttributesListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadAttributesListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about attributes of the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadSignWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about road signs on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">`RoadSignWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadSignWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">`RoadTextsListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadTextsListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about the textual attributes of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoute ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the route that is being navigated.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">`RouteDeviationListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteDeviationListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies when deviation from the route is observed.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteDrawOrder ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The draw order of the polylines representing the route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-drawordertype" title="enum class in com.here.sdk.mapview">`DrawOrderType`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteDrawOrderType ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The draw order type of the polylines representing the route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">`RouteProgressListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteProgressListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener that notifies when a route progress change occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSafetyCameraWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive safety camera warning notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">`SafetyCameraWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSafetyCameraWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets safety camera warning options to be passed to SafetyCameraWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">`SchoolZoneWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSchoolZoneWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about school zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">`SchoolZoneWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSchoolZoneWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">`SpeedLimitListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedLimitListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about the speed limit of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">`SpeedWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">`SpeedWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the speed warning options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">`TollStopWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTollStopWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about the the upcoming toll stop.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">`TransportProfile`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      getTrackingTransportProfile ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">`TransportSpecification`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrackingTransportSpecification ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the transport specification for the Navigator , when no route is present.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficMergeWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about merging traffic to the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">`TrafficMergeWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficMergeWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">`TrafficOnRoute`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficOnRoute ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the traffic information for the current route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTruckRestrictionsWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the listener to receive notifications about truck restrictions on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">`TruckRestrictionsWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTruckRestrictionsWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">`WarnerEngine`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWarnerEngine ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the warner engine used by the navigator.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWarningNotificationDistances ( WarningType warningType)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the warning notification distances for the requested warning type.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isDebugModeEnabled ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current debug mode state.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isDynamicFrameRateEnabled ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Controls whether the number of map updates is dynamically calculated based on the current zoom level.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isEnableTunnelExtrapolation ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Return true if tunnel extrapolation is enabled otherwise false .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isExtrapolationEnabled ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state of the position extrapolation logic.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isLocationAccuracyVisualized ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a boolean indicating if the halo accuracy visualization of the default LocationIndicator is rendered or not.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isManeuverArrowsVisible ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state of maneuver arrow rendering during visual navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isOffRoadDestinationVisible ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state of off-road destination visualization during visual navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isPassthroughWaypointsHandlingEnabled ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Return true if handling of passthrough waypoints is enabled, otherwise - false .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isRendering ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a value indicating whether visual navigation rendering is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isRouteProgressVisible ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state of route progress during visual navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isRouteVisible ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state of route rendering during visual navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isTrafficOnRouteVisible ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current state whether traffic conditions on route should be displayed during visual navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onLocationUpdated ( Location location)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Called each time a new location is available.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      repeatLastManeuverNotification ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBorderCrossingWarningListener ( BorderCrossingWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about border crossings on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBorderCrossingWarningOptions ( BorderCrossingWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets border crossing warning options to be passed to BorderCrossingWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCameraBehavior ( CameraBehavior value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets how the VisualNavigator handles the camera.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setColors ( VisualNavigatorColors value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets an object containing colors used to render route progress and maneuver arrow visualization.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCurrentSituationLaneAssistanceViewListener ( CurrentSituationLaneAssistanceViewListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive current situation lane assistance view notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomLocationIndicator ( LocationIndicator value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom LocationIndicator , so that VisualNavigator uses the provided one instead of the default.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomOption ( String key, String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This method sets custom options that controls navigator behavior.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDangerZoneWarningListener ( DangerZoneWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive current danger zones notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDebugGpxFilePath ( String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the path of a GPX file to be displayed on the map.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDebugModeEnabled (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to enable debug mode or not.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDestinationReachedListener ( DestinationReachedListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notify when the destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDynamicFrameRateEnabled (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Controls whether the number of map updates is dynamically calculated based on the current zoom level.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEnableTunnelExtrapolation (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Set to true to enable tunnel extrapolation, set to false to disable tunnel extrapolation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEnvironmentalZoneWarningListener ( EnvironmentalZoneWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive current environmental zones notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEventTextListener ( EventTextListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies when a text notification is available.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setEventTextOptions ( EventTextOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the text notification options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setExtrapolationEnabled (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to enable or disable the position extrapolation logic.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setGuidanceFrameRate (int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frame rate used during guidance.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setInterpolatedLocationListener ( InterpolatedLocationListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that receives interpolated locations.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setJunctionViewLaneAssistanceListener ( JunctionViewLaneAssistanceListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive junction view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLocationAccuracyVisualized (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the halo accuracy visualization of the default LocationIndicator .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLowSpeedZoneWarningListener ( LowSpeedZoneWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about low speed zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverArrowsVisible (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to perform maneuver arrow rendering during visual navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverArrowWidthFactor (double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the factor that multiplies the width of the maneuver arrow defined by the getMeasureDependentWidth() .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverNotificationOptions ( ManeuverNotificationOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the maneuver notification options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverNotificationTimingOptions ( TransportMode transportMode, TimingProfile timingProfile, ManeuverNotificationTimingOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Set timing option values for the combination of transport mode and timing profile.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverViewLaneAssistanceListener ( ManeuverViewLaneAssistanceListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive maneuver view lane assistance notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMeasureDependentWidth ( Map < MapMeasure , Double > value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the MapMeasure dependent route and maneuver arrows width in pixels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMilestoneStatusListener ( MilestoneStatusListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies when a Milestone has been reached or missed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setNavigableLocationListener ( NavigableLocationListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies current location updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOffRoadDestinationReachedListener ( OffRoadDestinationReachedListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies when the off-road destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOffRoadDestinationVisible (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to show a dashed line between the map-matched and the original destination which is off-road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOffRoadProgressListener ( OffRoadProgressListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies about off-road progress.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPassthroughWaypointsHandlingEnabled (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Set to true enables handling of passthrough waypoints, set to false disables handling of passthrough waypoints.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPostActionListener ( PostActionListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive post action notifications, such as a charge action at a charging station.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRailwayCrossingWarningListener ( RailwayCrossingWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about railway crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRealisticViewWarningListener ( RealisticViewWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about junction views on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRealisticViewWarningOptions ( RealisticViewWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoadAttributesListener ( RoadAttributesListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about attributes of the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoadSignWarningListener ( RoadSignWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about road signs on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoadSignWarningOptions ( RoadSignWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoadTextsListener ( RoadTextsListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about the textual attributes of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoute ( Route value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the route to navigate.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteDeviationListener ( RouteDeviationListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies when deviation from the route is observed.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteDrawOrder (int value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The draw order of the polylines representing the route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteDrawOrderType ( DrawOrderType value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The draw order type of the polylines representing the route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteProgressListener ( RouteProgressListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener that notifies when a route progress change occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteProgressVisible (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to perform route progress coloring ("eat-up") during visual navigation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteVisible (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to perform route rendering during visual navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSafetyCameraWarningListener ( SafetyCameraWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive safety camera warning notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSafetyCameraWarningOptions ( SafetyCameraWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets safety camera warning options to be passed to SafetyCameraWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSchoolZoneWarningListener ( SchoolZoneWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about school zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSchoolZoneWarningOptions ( SchoolZoneWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSpeedLimitListener ( SpeedLimitListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about the speed limit of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSpeedWarningListener ( SpeedWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSpeedWarningOptions ( SpeedWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the speed warning options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTollStopWarningListener ( TollStopWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about the upcoming toll stop.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      setTrackingTransportProfile ( TransportProfile value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrackingTransportSpecification ( TransportSpecification value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the transport specification for the Navigator , when no route is present.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficMergeWarningListener ( TrafficMergeWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about merging traffic to the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficMergeWarningOptions ( TrafficMergeWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficOnRoute ( TrafficOnRoute value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the traffic information for the current route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficOnRouteVisible (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether to perform rendering of traffic conditions on the route when Route visualization is enabled during visual navigation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTruckRestrictionsWarningListener ( TruckRestrictionsWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the listener to receive notifications about truck restrictions on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTruckRestrictionsWarningOptions ( TruckRestrictionsWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWarningNotificationDistances ( WarningType warningType, WarningNotificationDistances warningNotificationDistances)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Set the warning notification distances for the specified warning types.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      startRendering ( MapViewBase mapView)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts visual navigation rendering.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stopRendering ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops visual navigation rendering.

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

    ### VisualNavigator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VisualNavigator</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> when operation fails.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### VisualNavigator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> when operation fails.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-NavigatorInterface" class="section detail">

    ### VisualNavigator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class using provided instance of NavigatorInterface as source of data. Note: The VisualNavigator implements the NavigatorInterface interface and forwards all calls to the underlying NavigatorInterface instance. When multiple VisualNavigator instances share the same NavigatorInterface instance, method calls on this common instance will overwrite changes made by another, which may lead to unexpected behavior. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `navigator` -

    A NavigatorInterface implementation instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> when operation fails.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-navigation-NavigatorInterface" class="section detail">

    ### VisualNavigator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class using provided instance of NavigatorInterface as source of data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    `navigator` -

    A NavigatorInterface implementation instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> when operation fails.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getAvailableLanguagesForManeuverNotifications" class="section detail">

    ### getAvailableLanguagesForManeuverNotifications

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a>\></span> <span class="element-name">getAvailableLanguagesForManeuverNotifications</span>()

    </div>

    <div class="block">

    Returns the list of languages for maneuver notification currently available in the SDK.

    </div>

    Returns:  
    the list of languages for maneuver notification currently available in the SDK.

    </div>

  - <div id="sdk-for-android-navigate-startRendering-com-here-sdk-mapview-MapViewBase" class="section detail">

    ### startRendering

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startRendering</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span>

    </div>

    <div class="block">

    Starts visual navigation rendering. A preconfigured current location marker is shown as soon as a location is received. The marker is chosen according to the transport mode specified in the route. If no route is present, the marker is chosen based on the NavigatorInterface.getTrackingTransportSpecification() property. Calling startRendering() changes the MapCamera.getPrincipalPoint() property so that the current position indicator is equal to the value from CameraBehavior.getNormalizedPrincipalPoint() , in which by default places the principal point slightly at the bottom of the mapview. It is restored to its original value when stopRendering() is called. Note: When rendering is started again for a new map view instance, rendering is automatically stopped on the previous map view instance. Also note that the MapViewBase.getFrameRate() can be lowered to reduce CPU usage, to adjust for tradeoffs between rendering smoothness versus battery consumption.

    </div>

    Parameters:  
    `mapView` -

    The map view on which visual navigation will take place.

    </div>

  - <div id="sdk-for-android-navigate-stopRendering" class="section detail">

    ### stopRendering

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stopRendering</span>()

    </div>

    <div class="block">

    Stops visual navigation rendering. This removes the current location marker. Other settings, like map orientation or camera distance, which may have been altered during rendering are no longer updated.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-defaultRouteManeuverArrowMeasureDependentWidths" class="section detail">

    ### defaultRouteManeuverArrowMeasureDependentWidths

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">defaultRouteManeuverArrowMeasureDependentWidths</span>()

    </div>

    <div class="block">

    Retrieves a dictionary of default route and maneuver arrow widths as a function of MapMeasure s.

    </div>

    Returns:  
    A dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>s.

    </div>

  - <div id="sdk-for-android-navigate-getCameraBehavior" class="section detail">

    ### getCameraBehavior

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span> <span class="element-name">getCameraBehavior</span>()

    </div>

    <div class="block">

    Gets the currently set camera behavior. Setting null disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when null is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of FixedCameraBehavior .

    </div>

    Returns:  
    Camera behavior which defines how the <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">`VisualNavigator`</a> handles the camera.

    </div>

  - <div id="sdk-for-android-navigate-setCameraBehavior-com-here-sdk-navigation-CameraBehavior" class="section detail">

    ### setCameraBehavior

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBehavior</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a> value)</span>

    </div>

    <div class="block">

    Sets how the VisualNavigator handles the camera. Setting null disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when null is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of FixedCameraBehavior .

    </div>

    Parameters:  
    `value` -

    Camera behavior which defines how the <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">`VisualNavigator`</a> handles the camera.

    </div>

  - <div id="sdk-for-android-navigate-isRouteVisible" class="section detail">

    ### isRouteVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRouteVisible</span>()

    </div>

    <div class="block">

    Gets the current state of route rendering during visual navigation. When enabled, the set Route will be rendered as a MapPolyline together with MapArrow items that indicate the next turns. By default, it is enabled. When disabled, MapArrow items are still rendered. To hide arrows, use VisualNavigatorColors with transparent color.

    </div>

    Returns:  
    `Route` visibility which defines whether to perform route rendering during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-setRouteVisible-boolean" class="section detail">

    ### setRouteVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to perform route rendering during visual navigation. When enabled, the set Route will be rendered as a MapPolyline together with MapArrow items that indicate the next turns. By default, it is enabled. When disabled, MapArrow items are still rendered. To hide arrows, use VisualNavigatorColors with transparent color.

    </div>

    Parameters:  
    `value` -

    `Route` visibility which defines whether to perform route rendering during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-isRouteProgressVisible" class="section detail">

    ### isRouteProgressVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRouteProgressVisible</span>()

    </div>

    <div class="block">

    Gets the current state of route progress during visual navigation. By default, it is enabled.

    </div>

    Returns:  
    `RouteProgress` visibility which defines whether to perform route progress coloring ("eat-up") during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-setRouteProgressVisible-boolean" class="section detail">

    ### setRouteProgressVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to perform route progress coloring ("eat-up") during visual navigation. By default, it is enabled.

    </div>

    Parameters:  
    `value` -

    `RouteProgress` visibility which defines whether to perform route progress coloring ("eat-up") during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-isManeuverArrowsVisible" class="section detail">

    ### isManeuverArrowsVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverArrowsVisible</span>()

    </div>

    <div class="block">

    Gets the current state of maneuver arrow rendering during visual navigation. By default, it is enabled.

    </div>

    Returns:  
    Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverArrowsVisible-boolean" class="section detail">

    ### setManeuverArrowsVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowsVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to perform maneuver arrow rendering during visual navigation. By default, it is enabled.

    </div>

    Parameters:  
    `value` -

    Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-isOffRoadDestinationVisible" class="section detail">

    ### isOffRoadDestinationVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOffRoadDestinationVisible</span>()

    </div>

    <div class="block">

    Gets the current state of off-road destination visualization during visual navigation. Note: The dashed line will be drawn only if the original destination is off-road.

    </div>

    Returns:  
    Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination which is off-road. By default it is enabled.

    </div>

  - <div id="sdk-for-android-navigate-setOffRoadDestinationVisible-boolean" class="section detail">

    ### setOffRoadDestinationVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadDestinationVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to show a dashed line between the map-matched and the original destination which is off-road. Note: The dashed line will be drawn only if the original destination is off-road.

    </div>

    Parameters:  
    `value` -

    Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination which is off-road. By default it is enabled.

    </div>

  - <div id="sdk-for-android-navigate-isTrafficOnRouteVisible" class="section detail">

    ### isTrafficOnRouteVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTrafficOnRouteVisible</span>()

    </div>

    <div class="block">

    Gets the current state whether traffic conditions on route should be displayed during visual navigation. When enabled the route's MapPolyline will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in VisualNavigatorColors.getTrafficOnRouteColors() . The presented traffic information is either set by the user via NavigatorInterface.getTrafficOnRoute() or is generated from historical traffic data stored in the map. Note: VisualNavigator does not perform automatic traffic data updates. The updated traffic information is available through the \[sdk.routing.RoutingEngine.calculate_traffic_on_route\] interface. The returned TrafficOnRoute could then be used to update \[sdk.navigation.NavigatorInterface.traffic_on_route\] to refresh the traffic on route visualization. Defaults to false .

    </div>

    Returns:  
    A boolean which defines whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficOnRouteVisible-boolean" class="section detail">

    ### setTrafficOnRouteVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRouteVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to perform rendering of traffic conditions on the route when Route visualization is enabled during visual navigation. When enabled the route's MapPolyline will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in VisualNavigatorColors.getTrafficOnRouteColors() . The presented traffic information is either set by the user via NavigatorInterface.getTrafficOnRoute() or is generated from historical traffic data stored in the map. Note: VisualNavigator does not perform automatic traffic data updates. The updated traffic information is available through the \[sdk.routing.RoutingEngine.calculate_traffic_on_route\] interface. The returned TrafficOnRoute could then be used to update \[sdk.navigation.NavigatorInterface.traffic_on_route\] to refresh the traffic on route visualization. Defaults to false .

    </div>

    Parameters:  
    `value` -

    A boolean which defines whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation.

    </div>

  - <div id="sdk-for-android-navigate-getCustomLocationIndicator" class="section detail">

    ### getCustomLocationIndicator

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a></span> <span class="element-name">getCustomLocationIndicator</span>()

    </div>

    <div class="block">

    Gets the currently set LocationIndicator . If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided LocationIndicator , since VisualNavigator will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is null , which means the default indicator is used, and VisualNavigator automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls.

    </div>

    Returns:  
    Custom location indicator <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">`LocationIndicator`</a> which <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">`VisualNavigator`</a> uses instead of the default.

    </div>

  - <div id="sdk-for-android-navigate-setCustomLocationIndicator-com-here-sdk-mapview-LocationIndicator" class="section detail">

    ### setCustomLocationIndicator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomLocationIndicator</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a> value)</span>

    </div>

    <div class="block">

    Sets a custom LocationIndicator , so that VisualNavigator uses the provided one instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided LocationIndicator , since VisualNavigator will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is null , which means the default indicator is used, and VisualNavigator automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls.

    </div>

    Parameters:  
    `value` -

    Custom location indicator <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">`LocationIndicator`</a> which <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">`VisualNavigator`</a> uses instead of the default.

    </div>

  - <div id="sdk-for-android-navigate-getInterpolatedLocationListener" class="section detail">

    ### getInterpolatedLocationListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a></span> <span class="element-name">getInterpolatedLocationListener</span>()

    </div>

    <div class="block">

    Gets the listener that receives interpolated locations. For example, to pan a second instance of a MapViewBase or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. For example, to pan a second instance of a MapViewBase or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. Defaults to null .

    </div>

    Returns:  
    Object to receive interpolated locations.

    </div>

  - <div id="sdk-for-android-navigate-setInterpolatedLocationListener-com-here-sdk-navigation-InterpolatedLocationListener" class="section detail">

    ### setInterpolatedLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInterpolatedLocationListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that receives interpolated locations. For example, to pan a second instance of a MapViewBase or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. Defaults to null .

    </div>

    Parameters:  
    `value` -

    Object to receive interpolated locations.

    </div>

  - <div id="sdk-for-android-navigate-isRendering" class="section detail">

    ### isRendering

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRendering</span>()

    </div>

    <div class="block">

    Returns a value indicating whether visual navigation rendering is enabled.

    </div>

    Returns:  
    Returns a value indicating whether visual navigation rendering is enabled.

    </div>

  - <div id="sdk-for-android-navigate-getColors" class="section detail">

    ### getColors

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">getColors</span>()

    </div>

    <div class="block">

    Gets an object containing colors used to render route progress and maneuver arrow visualization. Setting a new instance overwrites the default color settings as specified in VisualNavigatorColors .

    </div>

    Returns:  
    Object containing colors used to render route progress and maneuver arrow visualization.

    </div>

  - <div id="sdk-for-android-navigate-setColors-com-here-sdk-navigation-VisualNavigatorColors" class="section detail">

    ### setColors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColors</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a> value)</span>

    </div>

    <div class="block">

    Sets an object containing colors used to render route progress and maneuver arrow visualization. Setting a new instance overwrites the default color settings as specified in VisualNavigatorColors .

    </div>

    Parameters:  
    `value` -

    Object containing colors used to render route progress and maneuver arrow visualization.

    </div>

  - <div id="sdk-for-android-navigate-getMeasureDependentWidth" class="section detail">

    ### getMeasureDependentWidth

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">getMeasureDependentWidth</span>()

    </div>

    <div class="block">

    Gets the MapMeasure dependent polyline and maneuver arrow width in pixels. It is a dictionary that has keys that are MapMeasure s and values that are width in pixels at this MapMeasure s. This route and maneuver arrows width is multiplied by a pixel_scale MapViewBase.getPixelScale() before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with setManeuverArrowWidthFactor ; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest MapMeasure , its corresponding value width is used. For keys above the highest MapMeasure , its corresponding value width is used. Only MapMeasure of \[sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL\] type are supported. MapMeasure of other unsupported types will be ignored. measureDependentWidth with a single entry is equivalent to use of the constant width value of this single entry for all MapMeasure s. Empty measureDependentWidth is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then measureDependentWidth contains predefined values chosen to be optimal for different route classes. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Returns:  
    The `measureDependentWidth` that defines the route and maneuver arrows width.

    </div>

  - <div id="sdk-for-android-navigate-setMeasureDependentWidth-java-util-Map" class="section detail">

    ### setMeasureDependentWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMeasureDependentWidth</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\> value)</span>

    </div>

    <div class="block">

    Sets the MapMeasure dependent route and maneuver arrows width in pixels. It is a dictionary that has keys that are MapMeasure s and values that are width in pixels at this MapMeasure s. This route and maneuver arrows width is multiplied by a pixel_scale MapViewBase.getPixelScale() before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with setManeuverArrowWidthFactor ; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest MapMeasure , its corresponding value width is used. For keys above the highest MapMeasure , its corresponding value width is used. Only MapMeasure of \[sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL\] type are supported. MapMeasure of other unsupported types will be ignored. measureDependentWidth with a single entry is equivalent to use of the constant width value of this single entry for all MapMeasure s. Empty measureDependentWidth is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then measureDependentWidth contains predefined values chosen to be optimal for different route classes. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    The `measureDependentWidth` that defines the route and maneuver arrows width.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverArrowWidthFactor" class="section detail">

    ### getManeuverArrowWidthFactor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getManeuverArrowWidthFactor</span>()

    </div>

    <div class="block">

    Gets the factor that multiplies width of the maneuver arrow defined by getMeasureDependentWidth() . By default it is set to one. The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.

    </div>

    Returns:  
    A factor of [](sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator#getMeasureDependentWidth())

        getMeasureDependentWidth()

    </a> defining the width of the maneuver arrow.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-setManeuverArrowWidthFactor-double" class="section detail">

    ### setManeuverArrowWidthFactor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowWidthFactor</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the factor that multiplies the width of the maneuver arrow defined by the getMeasureDependentWidth() . The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.

    </div>

    Parameters:  
    `value` -

    A factor of [](sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator#getMeasureDependentWidth())

        getMeasureDependentWidth()

    </a> defining the width of the maneuver arrow.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-isExtrapolationEnabled" class="section detail">

    ### isExtrapolationEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExtrapolationEnabled</span>()

    </div>

    <div class="block">

    Gets the current state of the position extrapolation logic. The predicted location follows the geometry of the route (or road) ahead. By default it is enabled.

    </div>

    Returns:  
    Defines whether the position extrapolation logic is enabled or not.

    </div>

  - <div id="sdk-for-android-navigate-setExtrapolationEnabled-boolean" class="section detail">

    ### setExtrapolationEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExtrapolationEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to enable or disable the position extrapolation logic. By default enabled. The predicted location follows the geometry of the route (or road) ahead. By default it is enabled.

    </div>

    Parameters:  
    `value` -

    Defines whether the position extrapolation logic is enabled or not.

    </div>

  - <div id="sdk-for-android-navigate-getDebugGpxFilePath" class="section detail">

    ### getDebugGpxFilePath

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getDebugGpxFilePath</span>()

    </div>

    <div class="block">

    Gets the path of the GPX file, is any available, currently being displayed on the map. Note: This API should be used for debugging purposes only.

    </div>

    Returns:  
    Show the contents of a GPX file on the map.

    </div>

  - <div id="sdk-for-android-navigate-setDebugGpxFilePath-java-lang-String" class="section detail">

    ### setDebugGpxFilePath

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDebugGpxFilePath</span><wbr></wbr><span class="parameters">(@Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets the path of a GPX file to be displayed on the map. Setting null removes it from the map. Note: This API should be used for debugging purposes only.

    </div>

    Parameters:  
    `value` -

    Show the contents of a GPX file on the map.

    </div>

  - <div id="sdk-for-android-navigate-isDebugModeEnabled" class="section detail">

    ### isDebugModeEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDebugModeEnabled</span>()

    </div>

    <div class="block">

    Gets the current debug mode state. A semi-transparent location marker indicating the map-matched location. A gray, semi-transparent location marker indicating the raw (or original) input location. A red polyline indicating the most probable path. A SVG overlay, on the middle-left of the screen, showing the following: IN - Input location: coordinates \[bearing\] \[speed\] \[accuracy\] RM - Route-matched location: coordinates bearing (distance-to-raw-location) MM - Map-Matched location: coordinates bearing (distance-to-raw-location) RM-MM - distance-between-route-and-map-matched-locations RP - Route progress: remaining-duration remaining-distance SP - Section progress: section-index/sections-count remaining-duration remaining-distance MP - Maneuver progress: maneuver-index remaining-duration remaining-distance CPU - CPU usage: cpu-usage current-date-time MS - Milestone status: section-index MISSED\|REACHED when RD - Route deviation: last-traveled-section-index last-traveled-section-distance when FPS - Frames per second: frames-per-second Fields between brackets (\[\]'s) are omitted if not available. Example: IN: 53.96880,14.77903 167° 8m/s RM: 53.96880,14.77903 167° (0.0m) MM: 53.96879,14.77903 167° (0.5m) RM-MM: 0.5m RP: 49h0m3s 4302km SP: 0/16 1h2m20s 58km MP: 1 5s 25m CPU: 7% 2024-01-01 13:21:59 MS: 1 REACHED 12:34:22 RD: 2 345m 11:13:55 FPS: 30.0 Note: This API should be used for debugging purposes only.

    </div>

    Returns:  
    When enabled, it shows useful information for debugging purposes.

    </div>

  - <div id="sdk-for-android-navigate-setDebugModeEnabled-boolean" class="section detail">

    ### setDebugModeEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDebugModeEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether to enable debug mode or not. A semi-transparent location marker indicating the map-matched location. A gray, semi-transparent location marker indicating the raw (or original) input location. A red polyline indicating the most probable path. A SVG overlay, on the middle-left of the screen, showing the following: IN - Input location: coordinates \[bearing\] \[speed\] \[accuracy\] RM - Route-matched location: coordinates bearing (distance-to-raw-location) MM - Map-Matched location: coordinates bearing (distance-to-raw-location) RM-MM - distance-between-route-and-map-matched-locations RP - Route progress: remaining-duration remaining-distance SP - Section progress: section-index/sections-count remaining-duration remaining-distance MP - Maneuver progress: maneuver-index remaining-duration remaining-distance CPU - CPU usage: cpu-usage current-date-time MS - Milestone status: section-index MISSED\|REACHED when RD - Route deviation: last-traveled-section-index last-traveled-section-distance when FPS - Frames per second: frames-per-second Fields between brackets (\[\]'s) are omitted if not available. Example: IN: 53.96880,14.77903 167° 8m/s RM: 53.96880,14.77903 167° (0.0m) MM: 53.96879,14.77903 167° (0.5m) RM-MM: 0.5m RP: 49h0m3s 4302km SP: 0/16 1h2m20s 58km MP: 1 5s 25m CPU: 7% 2024-01-01 13:21:59 MS: 1 REACHED 12:34:22 RD: 2 345m 11:13:55 FPS: 30.0 Note: This API should be used for debugging purposes only.

    </div>

    Parameters:  
    `value` -

    When enabled, it shows useful information for debugging purposes.

    </div>

  - <div id="sdk-for-android-navigate-isLocationAccuracyVisualized" class="section detail">

    ### isLocationAccuracyVisualized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLocationAccuracyVisualized</span>()

    </div>

    <div class="block">

    Gets a boolean indicating if the halo accuracy visualization of the default LocationIndicator is rendered or not. Does not affect halo accuracy indicator of the getCustomLocationIndicator() . If getCustomLocationIndicator() is set, then its halo accuracy indicator can be controlled using LocationIndicator.isAccuracyVisualized() .

    </div>

    Returns:  
    Controls if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">`LocationIndicator`</a> is rendered or not.

    </div>

  - <div id="sdk-for-android-navigate-setLocationAccuracyVisualized-boolean" class="section detail">

    ### setLocationAccuracyVisualized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocationAccuracyVisualized</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets the halo accuracy visualization of the default LocationIndicator . Does not affect halo accuracy indicator of the getCustomLocationIndicator() . If getCustomLocationIndicator() is set, then its halo accuracy indicator can be controlled using LocationIndicator.isAccuracyVisualized() .

    </div>

    Parameters:  
    `value` -

    Controls if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview">`LocationIndicator`</a> is rendered or not.

    </div>

  - <div id="sdk-for-android-navigate-isDynamicFrameRateEnabled" class="section detail">

    ### isDynamicFrameRateEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDynamicFrameRateEnabled</span>()

    </div>

    <div class="block">

    Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

    </div>

    Returns:  
    Flag used to enable or disable the dynamic frame rate.

    </div>

  - <div id="sdk-for-android-navigate-setDynamicFrameRateEnabled-boolean" class="section detail">

    ### setDynamicFrameRateEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDynamicFrameRateEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

    </div>

    Parameters:  
    `value` -

    Flag used to enable or disable the dynamic frame rate.

    </div>

  - <div id="sdk-for-android-navigate-getGuidanceFrameRate" class="section detail">

    ### getGuidanceFrameRate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGuidanceFrameRate</span>()

    </div>

    <div class="block">

    Frame rate used during guidance. Default is 30fps.

    </div>

    Returns:  
    Frame rate used during guidance.

    </div>

  - <div id="sdk-for-android-navigate-setGuidanceFrameRate-int" class="section detail">

    ### setGuidanceFrameRate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGuidanceFrameRate</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Frame rate used during guidance. Default is 30fps.

    </div>

    Parameters:  
    `value` -

    Frame rate used during guidance.

    </div>

  - <div id="sdk-for-android-navigate-getRouteDrawOrder" class="section detail">

    ### getRouteDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getRouteDrawOrder</span>()

    </div>

    <div class="block">

    The draw order of the polylines representing the route. For more details see MapPolyline.getDrawOrder() . The default is 0.

    </div>

    Returns:  
    The draw order of the polylines representing the route.

    </div>

  - <div id="sdk-for-android-navigate-setRouteDrawOrder-int" class="section detail">

    ### setRouteDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDrawOrder</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    The draw order of the polylines representing the route. For more details see MapPolyline.getDrawOrder() . The default is 0.

    </div>

    Parameters:  
    `value` -

    The draw order of the polylines representing the route.

    </div>

  - <div id="sdk-for-android-navigate-getRouteDrawOrderType" class="section detail">

    ### getRouteDrawOrderType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></span> <span class="element-name">getRouteDrawOrderType</span>()

    </div>

    <div class="block">

    The draw order type of the polylines representing the route. For more details see MapPolyline.getDrawOrderType() . The default is DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT .

    </div>

    Returns:  
    The draw order type of the polylines representing the route.

    </div>

  - <div id="sdk-for-android-navigate-setRouteDrawOrderType-com-here-sdk-mapview-DrawOrderType" class="section detail">

    ### setRouteDrawOrderType

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDrawOrderType</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</span>

    </div>

    <div class="block">

    The draw order type of the polylines representing the route. For more details see MapPolyline.getDrawOrderType() . The default is DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT .

    </div>

    Parameters:  
    `value` -

    The draw order type of the polylines representing the route.

    </div>

  - <div id="sdk-for-android-navigate-getManeuver-int" class="section detail">

    ### getManeuver

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span class="element-name">getManeuver</span><wbr></wbr><span class="parameters">(int index)</span>

    </div>

    <div class="block">

    Returns maneuver at the given index.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getManeuver(int">`getManeuver`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `index` -

    The index of maneuver requested.

    Returns:  
    The maneuver if it exists or otherwise `null`.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverNotificationTimingOptions-com-here-sdk-transport-TransportMode-com-here-sdk-navigation-TimingProfile" class="section detail">

    ### getManeuverNotificationTimingOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></span> <span class="element-name">getManeuverNotificationTimingOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</span>

    </div>

    <div class="block">

    Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile">`getManeuverNotificationTimingOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `transportMode` -

    The transport mode of the timing options.

    `timingProfile` -

    The timing profile of the timing options.

    Returns:  
    The timing options with default values.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverNotificationTimingOptions-com-here-sdk-transport-TransportMode-com-here-sdk-navigation-TimingProfile-com-here-sdk-navigation-ManeuverNotificationTimingOptions" class="section detail">

    ### setManeuverNotificationTimingOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setManeuverNotificationTimingOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</span>

    </div>

    <div class="block">

    Set timing option values for the combination of transport mode and timing profile.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions">`setManeuverNotificationTimingOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `transportMode` -

    The transport mode of the timing options.

    `timingProfile` -

    The timing profile of the timing options.

    `options` -

    The timing options.

    Returns:  
    `True` if set successfully, `false` when options has invalid value, see <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationTimingOptions`</a> for more details about options.

    </div>

  - <div id="sdk-for-android-navigate-getWarningNotificationDistances-com-here-sdk-navigation-WarningType" class="section detail">

    ### getWarningNotificationDistances

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span>

    </div>

    <div class="block">

    Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling setWarningNotificationDistances function with the same warning type and the modified warning notification distances object.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getWarningNotificationDistances(com.here.sdk.navigation.WarningType">`getWarningNotificationDistances`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `warningType` -

    The warning type for which the notification distances will be returned.

    Returns:  
    The notification distances for the given warning type.

    </div>

  - <div id="sdk-for-android-navigate-setWarningNotificationDistances-com-here-sdk-navigation-WarningType-com-here-sdk-navigation-WarningNotificationDistances" class="section detail">

    ### setWarningNotificationDistances

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span>

    </div>

    <div class="block">

    Set the warning notification distances for the specified warning types. Note: The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use NavigatorInterface.school_zone_warning_options instead. Attempting to set the warning notification distances for the school zone warner using the NavigatorInterface.set_warning_notification_distances method will fail and return false . Always use SchoolZoneWarningOptions.warning_distance_in_meters to set the warning notification distance for the school zone warner regardless of the TimingProfile . If NavigatorInterface.set_warning_notification_distances could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the NavigatorInterface.set_warning_notification_distances method will fail and return false . Always use TrafficMergeWarningOptions.warning_distance_in_meters to set the warning notification distance for the traffic merge warner regardless of the TimingProfile . Using the NavigatorInterface.set_warning_notification_distances method will fail and return false to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances">`setWarningNotificationDistances`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `warningType` -

    The warning type for which the warning notification distances will be set.

    `warningNotificationDistances` -

    The warning notification distances to be set for the specified warning types.

    Returns:  
    `True` if set successfully, `false` when the warning_type is \[WarningType.SCHOOL_ZONE\] or the options have invalid values, see <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a> for more details about warning notification distances.

    </div>

  - <div id="sdk-for-android-navigate-repeatLastManeuverNotification" class="section detail">

    ### repeatLastManeuverNotification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">repeatLastManeuverNotification</span>()

    </div>

    <div class="block">

    Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#repeatLastManeuverNotification(">`repeatLastManeuverNotification`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    </div>

  - <div id="sdk-for-android-navigate-calculateRemainingDistanceInMeters-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### calculateRemainingDistanceInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">calculateRemainingDistanceInMeters</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span>

    </div>

    <div class="block">

    This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates">`calculateRemainingDistanceInMeters`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the location.

    Returns:  
    distance in meters or null if given coordinates are not on route or given coordinates were already traversed.

    </div>

  - <div id="sdk-for-android-navigate-setCustomOption-java-lang-String-java-lang-String" class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomOption</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setCustomOption(java.lang.String,java.lang.String">`setCustomOption`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `key` -

    Option name

    `value` -

    New option value

    </div>

  - <div id="sdk-for-android-navigate-onLocationUpdated-com-here-sdk-core-Location" class="section detail">

    ### onLocationUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span>

    </div>

    <div class="block">

    Called each time a new location is available. In a navigation context while using the Navigator or VisualNavigator , it's required to set the Location.time parameter for each Location object so that the HERE SDK can map-match the locations properly. If the Location.time parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the bearing and speed parameters for each Location object. Invoked on the main thread.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener#onLocationUpdated(com.here.sdk.core.Location">`onLocationUpdated`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

    Parameters:  
    `location` -

    Current location.

    </div>

  - <div id="sdk-for-android-navigate-getRoute" class="section detail">

    ### getRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()

    </div>

    <div class="block">

    Gets the route that is being navigated. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through NavigableLocationListener . If set, both route progress ( RouteProgressListener ) and route deviation ( RouteDeviationListener ) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRoute(">`getRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    The route to navigate.

    </div>

  - <div id="sdk-for-android-navigate-setRoute-com-here-sdk-routing-Route" class="section detail">

    ### setRoute

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoute</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span>

    </div>

    <div class="block">

    Sets the route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through NavigableLocationListener . If set, both route progress ( RouteProgressListener ) and route deviation ( RouteDeviationListener ) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRoute(com.here.sdk.routing.Route">`setRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    The route to navigate.

    </div>

  - <div id="sdk-for-android-navigate-getTrackingTransportProfile" class="section detail">

    ### getTrackingTransportProfile

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></span> <span class="element-name">getTrackingTransportProfile</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.

    </div>

    </div>

    <div class="block">

    Gets the transport profile for the Navigator , when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a TransportProfile can be defined with a VehicleProfile . A vehicle profile can have several parameters such as VehicleType to set the source of information describing the vehicle. The default is a VehicleType.CAR profile. Currently used members of TransportProfile VehicleType : Sets the transport mode. From vehicleProfile : grossWeightInKilograms : Required for truck related speed information. heightInCentimeters : Required for truck related speed information. widthInCentimeters : Additional truck definition for more specific truck speed information. lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTrackingTransportProfile(">`getTrackingTransportProfile`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-setTrackingTransportProfile-com-here-sdk-core-TransportProfile" class="section detail">

    ### setTrackingTransportProfile

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrackingTransportProfile</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.

    </div>

    </div>

    <div class="block">

    Sets the transport profile for the Navigator , when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a TransportProfile can be defined with a VehicleProfile . A vehicle profile can have several parameters such as VehicleType to set the source of information describing the vehicle. The default is a VehicleType.CAR profile. Currently used members of TransportProfile VehicleType : Sets the transport mode. From vehicleProfile : grossWeightInKilograms : Required for truck related speed information. heightInCentimeters : Required for truck related speed information. widthInCentimeters : Additional truck definition for more specific truck speed information. lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTrackingTransportProfile(com.here.sdk.core.TransportProfile">`setTrackingTransportProfile`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-getTrackingTransportSpecification" class="section detail">

    ### getTrackingTransportSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">getTrackingTransportSpecification</span>()

    </div>

    <div class="block">

    Gets the transport specification for the Navigator , when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An TransportSpecification must have the TransportSpecification.transportMode set. A transport specification can have several parameters defined such as VehicleSpecification.lengthInCentimeters defined in TransportSpecification.vehicleSpecification to set the source of information describing the vehicle. By default the TransportSpecification will have the transport mode set to TransportMode.CAR . Currently used members of TransportSpecification TransportSpecification.transportMode : Sets the transport mode. From TransportSpecification.vehicleSpecification : VehicleSpecification.grossWeightInKilograms : Required for truck related speed information. VehicleSpecification.heightInCentimeters : Required for truck related speed information. VehicleSpecification.widthInCentimeters : Additional truck definition for more specific truck speed information. VehicleSpecification.lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTrackingTransportSpecification(">`getTrackingTransportSpecification`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-setTrackingTransportSpecification-com-here-sdk-transport-TransportSpecification" class="section detail">

    ### setTrackingTransportSpecification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrackingTransportSpecification</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</span>

    </div>

    <div class="block">

    Sets the transport specification for the Navigator , when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An TransportSpecification must have the TransportSpecification.transportMode set. A transport specification can have several parameters defined such as VehicleSpecification.lengthInCentimeters defined in TransportSpecification.vehicleSpecification to set the source of information describing the vehicle. By default the TransportSpecification will have the transport mode set to TransportMode.CAR . Currently used members of TransportSpecification TransportSpecification.transportMode : Sets the transport mode. From TransportSpecification.vehicleSpecification : VehicleSpecification.grossWeightInKilograms : Required for truck related speed information. VehicleSpecification.heightInCentimeters : Required for truck related speed information. VehicleSpecification.widthInCentimeters : Additional truck definition for more specific truck speed information. VehicleSpecification.lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification">`setTrackingTransportSpecification`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-getNavigableLocationListener" class="section detail">

    ### getNavigableLocationListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></span> <span class="element-name">getNavigableLocationListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies current location updates. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getNavigableLocationListener(">`getNavigableLocationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about the current location.

    </div>

  - <div id="sdk-for-android-navigate-setNavigableLocationListener-com-here-sdk-navigation-NavigableLocationListener" class="section detail">

    ### setNavigableLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNavigableLocationListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies current location updates. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener">`setNavigableLocationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about the current location.

    </div>

  - <div id="sdk-for-android-navigate-getRouteProgressListener" class="section detail">

    ### getRouteProgressListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></span> <span class="element-name">getRouteProgressListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a route progress change occurs. Route progress notifications only occurs if the route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRouteProgressListener(">`getRouteProgressListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about navigation route progress.

    </div>

  - <div id="sdk-for-android-navigate-setRouteProgressListener-com-here-sdk-navigation-RouteProgressListener" class="section detail">

    ### setRouteProgressListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a route progress change occurs. Route progress notifications only occurs if the route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener">`setRouteProgressListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about navigation route progress.

    </div>

  - <div id="sdk-for-android-navigate-getRouteDeviationListener" class="section detail">

    ### getRouteDeviationListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></span> <span class="element-name">getRouteDeviationListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when deviation from the route is observed. Route deviation notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRouteDeviationListener(">`getRouteDeviationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about deviations from the route if any occurs.

    </div>

  - <div id="sdk-for-android-navigate-setRouteDeviationListener-com-here-sdk-navigation-RouteDeviationListener" class="section detail">

    ### setRouteDeviationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDeviationListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when deviation from the route is observed. Route deviation notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener">`setRouteDeviationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about deviations from the route if any occurs.

    </div>

  - <div id="sdk-for-android-navigate-getEventTextListener" class="section detail">

    ### getEventTextListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></span> <span class="element-name">getEventTextListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a text notification is available. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user. Note: In order to receive the text notification emitted for the traffic merge warner, when TrafficMergeWarningOptions.enable_text_notification has been enabled, the sdk.navigation.EventTextListener must be enabled as well.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getEventTextListener(">`getEventTextListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive text notifications when they are available.

    </div>

  - <div id="sdk-for-android-navigate-setEventTextListener-com-here-sdk-navigation-EventTextListener" class="section detail">

    ### setEventTextListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEventTextListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a text notification is available. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user. Note: In order to receive the text notification emitted for the traffic merge warner, when TrafficMergeWarningOptions.enable_text_notification has been enabled, the sdk.navigation.EventTextListener must be enabled as well.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setEventTextListener(com.here.sdk.navigation.EventTextListener">`setEventTextListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive text notifications when they are available.

    </div>

  - <div id="sdk-for-android-navigate-getMilestoneStatusListener" class="section detail">

    ### getMilestoneStatusListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></span> <span class="element-name">getMilestoneStatusListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a Milestone has been reached or missed. It informs on all waypoints (passed or missed) that are of type MilestoneType.STOPOVER but excludes the starting waypoint. Waypoints of type MilestoneType.PASSTHROUGH are excluded, by default, but can be included via NavigatorInterface.isPassthroughWaypointsHandlingEnabled() . Milestone status notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getMilestoneStatusListener(">`getMilestoneStatusListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a> or missing it.

    </div>

  - <div id="sdk-for-android-navigate-setMilestoneStatusListener-com-here-sdk-navigation-MilestoneStatusListener" class="section detail">

    ### setMilestoneStatusListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMilestoneStatusListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a Milestone has been reached or missed. It informs on all waypoints (passed or missed) that are of type MilestoneType.STOPOVER but excludes the starting waypoint. Waypoints of type MilestoneType.PASSTHROUGH are excluded, by default, but can be included via NavigatorInterface.isPassthroughWaypointsHandlingEnabled() . Milestone status notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener">`setMilestoneStatusListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a> or missing it.

    </div>

  - <div id="sdk-for-android-navigate-getDestinationReachedListener" class="section detail">

    ### getDestinationReachedListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></span> <span class="element-name">getDestinationReachedListener</span>()

    </div>

    <div class="block">

    Gets the listener that notify when the destination has been reached. Destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getDestinationReachedListener(">`getDestinationReachedListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive the notification about the arrival at the destination.

    </div>

  - <div id="sdk-for-android-navigate-setDestinationReachedListener-com-here-sdk-navigation-DestinationReachedListener" class="section detail">

    ### setDestinationReachedListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDestinationReachedListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notify when the destination has been reached. Destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener">`setDestinationReachedListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive the notification about the arrival at the destination.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedWarningListener" class="section detail">

    ### getSpeedWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></span> <span class="element-name">getSpeedWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSpeedWarningListener(">`getSpeedWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedWarningListener-com-here-sdk-navigation-SpeedWarningListener" class="section detail">

    ### setSpeedWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener">`setSpeedWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverViewLaneAssistanceListener" class="section detail">

    ### getManeuverViewLaneAssistanceListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></span> <span class="element-name">getManeuverViewLaneAssistanceListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getManeuverViewLaneAssistanceListener(">`getManeuverViewLaneAssistanceListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive maneuver view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverViewLaneAssistanceListener-com-here-sdk-navigation-ManeuverViewLaneAssistanceListener" class="section detail">

    ### setManeuverViewLaneAssistanceListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverViewLaneAssistanceListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener">`setManeuverViewLaneAssistanceListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive maneuver view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-getCurrentSituationLaneAssistanceViewListener" class="section detail">

    ### getCurrentSituationLaneAssistanceViewListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></span> <span class="element-name">getCurrentSituationLaneAssistanceViewListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current situation lane assistance view notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getCurrentSituationLaneAssistanceViewListener(">`getCurrentSituationLaneAssistanceViewListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive current situation lane assistance view notifications.

    </div>

  - <div id="sdk-for-android-navigate-setCurrentSituationLaneAssistanceViewListener-com-here-sdk-navigation-CurrentSituationLaneAssistanceViewListener" class="section detail">

    ### setCurrentSituationLaneAssistanceViewListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrentSituationLaneAssistanceViewListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current situation lane assistance view notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener">`setCurrentSituationLaneAssistanceViewListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive current situation lane assistance view notifications.

    </div>

  - <div id="sdk-for-android-navigate-getEnvironmentalZoneWarningListener" class="section detail">

    ### getEnvironmentalZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></span> <span class="element-name">getEnvironmentalZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current environmental zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getEnvironmentalZoneWarningListener(">`getEnvironmentalZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notification on approaching environmental zones.

    </div>

  - <div id="sdk-for-android-navigate-setEnvironmentalZoneWarningListener-com-here-sdk-navigation-EnvironmentalZoneWarningListener" class="section detail">

    ### setEnvironmentalZoneWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnvironmentalZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current environmental zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener">`setEnvironmentalZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notification on approaching environmental zones.

    </div>

  - <div id="sdk-for-android-navigate-getJunctionViewLaneAssistanceListener" class="section detail">

    ### getJunctionViewLaneAssistanceListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></span> <span class="element-name">getJunctionViewLaneAssistanceListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getJunctionViewLaneAssistanceListener(">`getJunctionViewLaneAssistanceListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive junction view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-setJunctionViewLaneAssistanceListener-com-here-sdk-navigation-JunctionViewLaneAssistanceListener" class="section detail">

    ### setJunctionViewLaneAssistanceListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setJunctionViewLaneAssistanceListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener">`setJunctionViewLaneAssistanceListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive junction view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSafetyCameraWarningListener" class="section detail">

    ### getSafetyCameraWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></span> <span class="element-name">getSafetyCameraWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive safety camera warning notifications. If a listener is present, notifications about safety speed cameras will be also sent via SafetyCameraWarningListener . Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSafetyCameraWarningListener(">`getSafetyCameraWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive safety camera warner notifications.

    </div>

  - <div id="sdk-for-android-navigate-setSafetyCameraWarningListener-com-here-sdk-navigation-SafetyCameraWarningListener" class="section detail">

    ### setSafetyCameraWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive safety camera warning notifications. If a listener is present, notifications about safety speed cameras will be also sent via SafetyCameraWarningListener . Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener">`setSafetyCameraWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive safety camera warner notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSafetyCameraWarningOptions" class="section detail">

    ### getSafetyCameraWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span class="element-name">getSafetyCameraWarningOptions</span>()

    </div>

    <div class="block">

    Gets safety camera warning options to be passed to SafetyCameraWarningListener . These options allow the enabling or disabling the text notification for the warner.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSafetyCameraWarningOptions(">`getSafetyCameraWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setSafetyCameraWarningOptions-com-here-sdk-navigation-SafetyCameraWarningOptions" class="section detail">

    ### setSafetyCameraWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets safety camera warning options to be passed to SafetyCameraWarningListener . These options allow the enabling or disabling the text notification for the warner.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions">`setSafetyCameraWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getDangerZoneWarningListener" class="section detail">

    ### getDangerZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></span> <span class="element-name">getDangerZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current danger zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getDangerZoneWarningListener(">`getDangerZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notification on approaching danger zones.

    </div>

  - <div id="sdk-for-android-navigate-setDangerZoneWarningListener-com-here-sdk-navigation-DangerZoneWarningListener" class="section detail">

    ### setDangerZoneWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDangerZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current danger zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener">`setDangerZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notification on approaching danger zones.

    </div>

  - <div id="sdk-for-android-navigate-getTruckRestrictionsWarningListener" class="section detail">

    ### getTruckRestrictionsWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></span> <span class="element-name">getTruckRestrictionsWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about truck restrictions on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTruckRestrictionsWarningListener(">`getTruckRestrictionsWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about truck restrictions on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setTruckRestrictionsWarningListener-com-here-sdk-navigation-TruckRestrictionsWarningListener" class="section detail">

    ### setTruckRestrictionsWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about truck restrictions on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener">`setTruckRestrictionsWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about truck restrictions on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getWarnerEngine" class="section detail">

    ### getWarnerEngine

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></span> <span class="element-name">getWarnerEngine</span>()

    </div>

    <div class="block">

    Gets the warner engine used by the navigator. This engine can be used to configure navigation warnings.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getWarnerEngine(">`getWarnerEngine`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Warner engine used by the navigator.

    </div>

  - <div id="sdk-for-android-navigate-getTruckRestrictionsWarningOptions" class="section detail">

    ### getTruckRestrictionsWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span class="element-name">getTruckRestrictionsWarningOptions</span>()

    </div>

    <div class="block">

    Gets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTruckRestrictionsWarningOptions(">`getTruckRestrictionsWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setTruckRestrictionsWarningOptions-com-here-sdk-navigation-TruckRestrictionsWarningOptions" class="section detail">

    ### setTruckRestrictionsWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions">`setTruckRestrictionsWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getPostActionListener" class="section detail">

    ### getPostActionListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></span> <span class="element-name">getPostActionListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getPostActionListener(">`getPostActionListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive post action notifications, such as a charge action at a charging station.

    </div>

  - <div id="sdk-for-android-navigate-setPostActionListener-com-here-sdk-navigation-PostActionListener" class="section detail">

    ### setPostActionListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPostActionListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setPostActionListener(com.here.sdk.navigation.PostActionListener">`setPostActionListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive post action notifications, such as a charge action at a charging station.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedLimitListener" class="section detail">

    ### getSpeedLimitListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></span> <span class="element-name">getSpeedLimitListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the speed limit of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSpeedLimitListener(">`getSpeedLimitListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about the speed limit of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedLimitListener-com-here-sdk-navigation-SpeedLimitListener" class="section detail">

    ### setSpeedLimitListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedLimitListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the speed limit of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener">`setSpeedLimitListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about the speed limit of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadTextsListener" class="section detail">

    ### getRoadTextsListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></span> <span class="element-name">getRoadTextsListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the textual attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRoadTextsListener(">`getRoadTextsListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about the textual attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadTextsListener-com-here-sdk-navigation-RoadTextsListener" class="section detail">

    ### setRoadTextsListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadTextsListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the textual attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener">`setRoadTextsListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about the textual attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadAttributesListener" class="section detail">

    ### getRoadAttributesListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></span> <span class="element-name">getRoadAttributesListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRoadAttributesListener(">`getRoadAttributesListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadAttributesListener-com-here-sdk-navigation-RoadAttributesListener" class="section detail">

    ### setRoadAttributesListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadAttributesListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener">`setRoadAttributesListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSignWarningListener" class="section detail">

    ### getRoadSignWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></span> <span class="element-name">getRoadSignWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about road signs on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRoadSignWarningListener(">`getRoadSignWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about road signs on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadSignWarningListener-com-here-sdk-navigation-RoadSignWarningListener" class="section detail">

    ### setRoadSignWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadSignWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about road signs on the current road. Note: This RoadSignWarningListener will provide school zone warnings only in case the speed limit inside the school zone is different than the default speed limit applicable for cars outside the school zone. For warnings about school zones regardless of their speed limits, the NavigatorInterface.road_sign_warning_listener should be used and the RoadSignWarning.type should be checked for value RoadSignType.SCHOOL_ZONE . The school zone warner is a zone warner, which means that for a school zone there will always be 3 warnings emitted, with the SchoolZoneWarning.distance_type set to DistanceType.AHEAD , DistanceType.REACHED Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener">`setRoadSignWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about road signs on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSignWarningOptions" class="section detail">

    ### getRoadSignWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span class="element-name">getRoadSignWarningOptions</span>()

    </div>

    <div class="block">

    Gets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRoadSignWarningOptions(">`getRoadSignWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setRoadSignWarningOptions-com-here-sdk-navigation-RoadSignWarningOptions" class="section detail">

    ### setRoadSignWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadSignWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions">`setRoadSignWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getSchoolZoneWarningListener" class="section detail">

    ### getSchoolZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></span> <span class="element-name">getSchoolZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about school zones on the current road. Setting null value to the listener will unset the listener. school zones on the current road. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSchoolZoneWarningListener(">`getSchoolZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about school zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setSchoolZoneWarningListener-com-here-sdk-navigation-SchoolZoneWarningListener" class="section detail">

    ### setSchoolZoneWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about school zones on the current road. Setting null value to the listener will unset the listener. school zones on the current road. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener">`setSchoolZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about school zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getSchoolZoneWarningOptions" class="section detail">

    ### getSchoolZoneWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span class="element-name">getSchoolZoneWarningOptions</span>()

    </div>

    <div class="block">

    Gets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener . It allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSchoolZoneWarningOptions(">`getSchoolZoneWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    School zone warning options

    </div>

  - <div id="sdk-for-android-navigate-setSchoolZoneWarningOptions-com-here-sdk-navigation-SchoolZoneWarningOptions" class="section detail">

    ### setSchoolZoneWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener . It allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions">`setSchoolZoneWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    School zone warning options

    </div>

  - <div id="sdk-for-android-navigate-getRealisticViewWarningListener" class="section detail">

    ### getRealisticViewWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></span> <span class="element-name">getRealisticViewWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about junction views on the current road. Setting null value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRealisticViewWarningListener(">`getRealisticViewWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about junction views on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRealisticViewWarningListener-com-here-sdk-navigation-RealisticViewWarningListener" class="section detail">

    ### setRealisticViewWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about junction views on the current road. Setting null value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener">`setRealisticViewWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about junction views on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRealisticViewWarningOptions" class="section detail">

    ### getRealisticViewWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span class="element-name">getRealisticViewWarningOptions</span>()

    </div>

    <div class="block">

    Gets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener . It allow to filter realistic views to be passed to RealisticViewWarningListener . This feature requires a map version greater or equal to 67 in order to function properly.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRealisticViewWarningOptions(">`getRealisticViewWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Realistic view warning options.

    </div>

  - <div id="sdk-for-android-navigate-setRealisticViewWarningOptions-com-here-sdk-navigation-RealisticViewWarningOptions" class="section detail">

    ### setRealisticViewWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener . It allow to filter realistic views to be passed to RealisticViewWarningListener . This feature requires a map version greater or equal to 67 in order to function properly.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions">`setRealisticViewWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Realistic view warning options.

    </div>

  - <div id="sdk-for-android-navigate-getBorderCrossingWarningListener" class="section detail">

    ### getBorderCrossingWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></span> <span class="element-name">getBorderCrossingWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getBorderCrossingWarningListener(">`getBorderCrossingWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about border crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setBorderCrossingWarningListener-com-here-sdk-navigation-BorderCrossingWarningListener" class="section detail">

    ### setBorderCrossingWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener">`setBorderCrossingWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about border crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getBorderCrossingWarningOptions" class="section detail">

    ### getBorderCrossingWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span class="element-name">getBorderCrossingWarningOptions</span>()

    </div>

    <div class="block">

    Gets border crossing warning options to be passed to BorderCrossingWarningListener . allow the filtering of the border crossing warnings received and set the notification distances.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getBorderCrossingWarningOptions(">`getBorderCrossingWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>. These options

    </div>

  - <div id="sdk-for-android-navigate-setBorderCrossingWarningOptions-com-here-sdk-navigation-BorderCrossingWarningOptions" class="section detail">

    ### setBorderCrossingWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets border crossing warning options to be passed to BorderCrossingWarningListener . allow the filtering of the border crossing warnings received and set the notification distances.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions">`setBorderCrossingWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>. These options

    </div>

  - <div id="sdk-for-android-navigate-getTollStopWarningListener" class="section detail">

    ### getTollStopWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></span> <span class="element-name">getTollStopWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the the upcoming toll stop. Setting null value to the listener will unset the listener. This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTollStopWarningListener(">`getTollStopWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive information on the upcoming toll stop.

    </div>

  - <div id="sdk-for-android-navigate-setTollStopWarningListener-com-here-sdk-navigation-TollStopWarningListener" class="section detail">

    ### setTollStopWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTollStopWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the upcoming toll stop. Setting null value to the listener will unset the listener. This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener">`setTollStopWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive information on the upcoming toll stop.

    </div>

  - <div id="sdk-for-android-navigate-getRailwayCrossingWarningListener" class="section detail">

    ### getRailwayCrossingWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></span> <span class="element-name">getRailwayCrossingWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getRailwayCrossingWarningListener(">`getRailwayCrossingWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about railway crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRailwayCrossingWarningListener-com-here-sdk-navigation-RailwayCrossingWarningListener" class="section detail">

    ### setRailwayCrossingWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRailwayCrossingWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener">`setRailwayCrossingWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about railway crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getLowSpeedZoneWarningListener" class="section detail">

    ### getLowSpeedZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></span> <span class="element-name">getLowSpeedZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available only for Japan. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getLowSpeedZoneWarningListener(">`getLowSpeedZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about low speed zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setLowSpeedZoneWarningListener-com-here-sdk-navigation-LowSpeedZoneWarningListener" class="section detail">

    ### setLowSpeedZoneWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLowSpeedZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available only for Japan. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener">`setLowSpeedZoneWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about low speed zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficMergeWarningListener" class="section detail">

    ### getTrafficMergeWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></span> <span class="element-name">getTrafficMergeWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about merging traffic to the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTrafficMergeWarningListener(">`getTrafficMergeWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive notifications about merging traffic to the current road.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficMergeWarningListener-com-here-sdk-navigation-TrafficMergeWarningListener" class="section detail">

    ### setTrafficMergeWarningListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about merging traffic to the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener">`setTrafficMergeWarningListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive notifications about merging traffic to the current road.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficMergeWarningOptions" class="section detail">

    ### getTrafficMergeWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span class="element-name">getTrafficMergeWarningOptions</span>()

    </div>

    <div class="block">

    Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTrafficMergeWarningOptions(">`getTrafficMergeWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficMergeWarningOptions-com-here-sdk-navigation-TrafficMergeWarningOptions" class="section detail">

    ### setTrafficMergeWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions">`setTrafficMergeWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getOffRoadDestinationReachedListener" class="section detail">

    ### getOffRoadDestinationReachedListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></span> <span class="element-name">getOffRoadDestinationReachedListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when the off-road destination has been reached. Off-road destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getOffRoadDestinationReachedListener(">`getOffRoadDestinationReachedListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive the notification about the arrival at the off-road destination.

    </div>

  - <div id="sdk-for-android-navigate-setOffRoadDestinationReachedListener-com-here-sdk-navigation-OffRoadDestinationReachedListener" class="section detail">

    ### setOffRoadDestinationReachedListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadDestinationReachedListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when the off-road destination has been reached. Off-road destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener">`setOffRoadDestinationReachedListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive the notification about the arrival at the off-road destination.

    </div>

  - <div id="sdk-for-android-navigate-getOffRoadProgressListener" class="section detail">

    ### getOffRoadProgressListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></span> <span class="element-name">getOffRoadProgressListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies about off-road progress. Off-road progress notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getOffRoadProgressListener(">`getOffRoadProgressListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Object to receive the notification about the off-road progress.

    </div>

  - <div id="sdk-for-android-navigate-setOffRoadProgressListener-com-here-sdk-navigation-OffRoadProgressListener" class="section detail">

    ### setOffRoadProgressListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadProgressListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies about off-road progress. Off-road progress notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener">`setOffRoadProgressListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Object to receive the notification about the off-road progress.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverNotificationOptions" class="section detail">

    ### getManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></span> <span class="element-name">getManeuverNotificationOptions</span>()

    </div>

    <div class="block">

    Gets the maneuver notification options. Notifications are only available if a route is present.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getManeuverNotificationOptions(">`getManeuverNotificationOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Options used for maneuver notifications.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverNotificationOptions-com-here-sdk-navigation-ManeuverNotificationOptions" class="section detail">

    ### setManeuverNotificationOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the maneuver notification options. Notifications are only available if a route is present.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions">`setManeuverNotificationOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Options used for maneuver notifications.

    </div>

  - <div id="sdk-for-android-navigate-getEventTextOptions" class="section detail">

    ### getEventTextOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></span> <span class="element-name">getEventTextOptions</span>()

    </div>

    <div class="block">

    Gets the text notification options. Notifications are only available if a route is present.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getEventTextOptions(">`getEventTextOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Options used for text notifications.

    </div>

  - <div id="sdk-for-android-navigate-setEventTextOptions-com-here-sdk-navigation-EventTextOptions" class="section detail">

    ### setEventTextOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEventTextOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the text notification options. Notifications are only available if a route is present.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setEventTextOptions(com.here.sdk.navigation.EventTextOptions">`setEventTextOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Options used for text notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedWarningOptions" class="section detail">

    ### getSpeedWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></span> <span class="element-name">getSpeedWarningOptions</span>()

    </div>

    <div class="block">

    Gets the speed warning options.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getSpeedWarningOptions(">`getSpeedWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Options used for the speed warning feature.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedWarningOptions-com-here-sdk-navigation-SpeedWarningOptions" class="section detail">

    ### setSpeedWarningOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the speed warning options.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions">`setSpeedWarningOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Options used for the speed warning feature.

    </div>

  - <div id="sdk-for-android-navigate-isEnableTunnelExtrapolation" class="section detail">

    ### isEnableTunnelExtrapolation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableTunnelExtrapolation</span>()

    </div>

    <div class="block">

    Return true if tunnel extrapolation is enabled otherwise false . By default the tunnel extrapolation is enabled.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#isEnableTunnelExtrapolation(">`isEnableTunnelExtrapolation`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Defines whether to enable or disable tunnel extrapolation.

    </div>

  - <div id="sdk-for-android-navigate-setEnableTunnelExtrapolation-boolean" class="section detail">

    ### setEnableTunnelExtrapolation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableTunnelExtrapolation</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Set to true to enable tunnel extrapolation, set to false to disable tunnel extrapolation. By default the tunnel extrapolation is enabled.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setEnableTunnelExtrapolation(boolean">`setEnableTunnelExtrapolation`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Defines whether to enable or disable tunnel extrapolation.

    </div>

  - <div id="sdk-for-android-navigate-isPassthroughWaypointsHandlingEnabled" class="section detail">

    ### isPassthroughWaypointsHandlingEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPassthroughWaypointsHandlingEnabled</span>()

    </div>

    <div class="block">

    Return true if handling of passthrough waypoints is enabled, otherwise - false . By default the handling of passthrough waypoints is disabled.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#isPassthroughWaypointsHandlingEnabled(">`isPassthroughWaypointsHandlingEnabled`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Defines whether to enable or disable handling of passthrough waypoints.

    </div>

  - <div id="sdk-for-android-navigate-setPassthroughWaypointsHandlingEnabled-boolean" class="section detail">

    ### setPassthroughWaypointsHandlingEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPassthroughWaypointsHandlingEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Set to true enables handling of passthrough waypoints, set to false disables handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setPassthroughWaypointsHandlingEnabled(boolean">`setPassthroughWaypointsHandlingEnabled`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Defines whether to enable or disable handling of passthrough waypoints.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficOnRoute" class="section detail">

    ### getTrafficOnRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></span> <span class="element-name">getTrafficOnRoute</span>()

    </div>

    <div class="block">

    Gets the traffic information for the current route. This impacts RouteProgress updates as the duration of the SectionProgress might change. However, the remaining distance and the route geometry will remain unchanged.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getTrafficOnRoute(">`getTrafficOnRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    Traffic information for the current route.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficOnRoute-com-here-sdk-routing-TrafficOnRoute" class="section detail">

    ### setTrafficOnRoute

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRoute</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</span>

    </div>

    <div class="block">

    Sets the traffic information for the current route. This impacts RouteProgress updates as the duration of the SectionProgress might change. However, the remaining distance and the route geometry will remain unchanged.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute">`setTrafficOnRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Parameters:  
    `value` -

    Traffic information for the current route.

    </div>

  - <div id="sdk-for-android-navigate-getLocationManager" class="section detail">

    ### getLocationManager

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></span> <span class="element-name">getLocationManager</span>()

    </div>

    <div class="block">

    Gets the location manager instance used by the navigator.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface#getLocationManager(">`getLocationManager`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a>

    Returns:  
    The location manager used by the navigator for map-matched location processing.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

