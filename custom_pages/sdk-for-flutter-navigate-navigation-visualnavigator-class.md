---
title: "VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VisualNavigator-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/VisualNavigator-class-sidebar.html">

<div>

# <span class="kind-class">VisualNavigator</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class provides all functionality of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a>.

In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, this class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>. Note that the VisualNavigator takes control of the MapView's (maximum) frame rate when rendering, i.e., between <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls. It overwrites the MapView's frame rate when some camera behavior is set using the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-guidanceframerate">VisualNavigator.guidanceFrameRate</a>. When no camera behavior is preset, the original MapView's frame rate (the value prior to the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> call) will be used. While the VisualNavigator is rendering, direct changes in the MapView's frame rate can lead to unexpected behavior and therefore should be avoided.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator">VisualNavigator</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator-withnavigator">VisualNavigator.withNavigator</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withNavigator-param-navigator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span> <span class="parameter-name">navigator</span></span>)</span>  
Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> as source of data.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator-withsdkengine">VisualNavigator.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator-withsdkengineandnavigator">VisualNavigator.withSdkEngineAndNavigator</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngineAndNavigator-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withSdkEngineAndNavigator-param-navigator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span> <span class="parameter-name">navigator</span></span>)</span>  
Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> as source of data.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener">borderCrossingWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span>  
Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about border crossings on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions">borderCrossingWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span>  
Border crossing warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances. Gets border crossing warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-camerabehavior">cameraBehavior</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>?</span>  
Camera behavior which defines how the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> handles the camera. Setting `null` disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when `null` is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of <a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a>. Gets the currently set camera behavior.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-colors">colors</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class">VisualNavigatorColors</a></span>  
Object containing colors used to render route progress and maneuver arrow visualization. Setting a new instance overwrites the default color settings as specified in `VisualNavigatorColors`. Gets an object containing colors used to render route progress and maneuver arrow visualization.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener">currentSituationLaneAssistanceViewListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span>  
Object to receive current situation lane assistance view notifications. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current situation lane assistance view notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator">customLocationIndicator</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>?</span>  
Custom location indicator <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> which <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> uses instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a>, since <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is `null`, which means the default indicator is used, and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls. Gets the currently set `LocationIndicator`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener">dangerZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span>  
Object to receive notification on approaching danger zones. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current danger zones notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-debuggpxfilepath">debugGpxFilePath</a></span> <span class="signature">↔ String?</span>  
Show the contents of a GPX file on the map. **Note:** This API should be used for debugging purposes only. Gets the path of the GPX file, is any available, currently being displayed on the map.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener">destinationReachedListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span>  
Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notify when the destination has been reached.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener">environmentalZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span>  
Object to receive notification on approaching environmental zones. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current environmental zones notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener">eventTextListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span>  
Object to receive text notifications when they are available. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. **Note:** In order to receive the text notification emitted for the traffic merge warner, when `TrafficMergeWarningOptions.enable_text_notification` has been enabled, the `sdk.navigation.EventTextListener` must be enabled as well. Gets the listener that notifies when a text notification is available.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions">eventTextOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span>  
Options used for text notifications. Notifications are only available if a route is present. Gets the text notification options.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-guidanceframerate">guidanceFrameRate</a></span> <span class="signature">↔ int</span>  
Frame rate used during guidance. Frame rate used during guidance. Default is 30fps.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-interpolatedlocationlistener">interpolatedLocationListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class">InterpolatedLocationListener</a>?</span>  
Object to receive interpolated locations. For example, to pan a second instance of a <a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a> or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. Defaults to `null`. Gets the listener that receives interpolated locations. For example, to pan a second instance of a <a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a> or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isdebugmodeenabled">isDebugModeEnabled</a></span> <span class="signature">↔ bool</span>  
When enabled, it shows useful information for debugging purposes.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isdynamicframerateenabled">isDynamicFrameRateEnabled</a></span> <span class="signature">↔ bool</span>  
Flag used to enable or disable the dynamic frame rate. Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation">isEnableTunnelExtrapolation</a></span> <span class="signature">↔ bool</span>  
Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled. Return `true` if tunnel extrapolation is enabled otherwise `false`.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isextrapolationenabled">isExtrapolationEnabled</a></span> <span class="signature">↔ bool</span>  
Defines whether the position extrapolation logic is enabled or not. The predicted location follows the geometry of the route (or road) ahead. By default it is enabled. Gets the current state of the position extrapolation logic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-islocationaccuracyvisualized">isLocationAccuracyVisualized</a></span> <span class="signature">↔ bool</span>  
Controls if the halo accuracy visualization of the default <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> is rendered or not. Does not affect halo accuracy indicator of the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator">VisualNavigator.customLocationIndicator</a>. If <a href="sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator">VisualNavigator.customLocationIndicator</a> is set, then its halo accuracy indicator can be controlled using <a href="sdk-for-flutter-navigate-mapview-locationindicator-isaccuracyvisualized">LocationIndicator.isAccuracyVisualized</a>. Gets a boolean indicating if the halo accuracy visualization of the default <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> is rendered or not.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-ismaneuverarrowsvisible">isManeuverArrowsVisible</a></span> <span class="signature">↔ bool</span>  
Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation. By default, it is enabled. Gets the current state of maneuver arrow rendering during visual navigation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isoffroaddestinationvisible">isOffRoadDestinationVisible</a></span> <span class="signature">↔ bool</span>  
Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination which is off-road. By default it is enabled. **Note:** The dashed line will be drawn only if the original destination is off-road. Gets the current state of off-road destination visualization during visual navigation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">isPassthroughWaypointsHandlingEnabled</a></span> <span class="signature">↔ bool</span>  
Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled. Return `true` if handling of passthrough waypoints is enabled, otherwise - `false`.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isrendering">isRendering</a></span> <span class="signature">→ bool</span>  
Returns a value indicating whether visual navigation rendering is enabled. Returns a value indicating whether visual navigation rendering is enabled.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isrouteprogressvisible">isRouteProgressVisible</a></span> <span class="signature">↔ bool</span>  
`RouteProgress` visibility which defines whether to perform route progress coloring ("eat-up") during visual navigation. By default, it is enabled. Gets the current state of route progress during visual navigation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-isroutevisible">isRouteVisible</a></span> <span class="signature">↔ bool</span>  
`Route` visibility which defines whether to perform route rendering during visual navigation. When enabled, the set `Route` will be rendered as a `MapPolyline` together with `MapArrow` items that indicate the next turns. By default, it is enabled. When disabled, `MapArrow` items are still rendered. To hide arrows, use `VisualNavigatorColors` with transparent color. Gets the current state of route rendering during visual navigation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-istrafficonroutevisible">isTrafficOnRouteVisible</a></span> <span class="signature">↔ bool</span>  
A boolean which defines whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation. When enabled the route's `MapPolyline` will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">VisualNavigatorColors.trafficOnRouteColors</a>. The presented traffic information is either set by the user via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">NavigatorInterface.trafficOnRoute</a> or is generated from historical traffic data stored in the map. **Note:** `VisualNavigator` does not perform automatic traffic data updates. The updated traffic information is available through the `sdk.routing.RoutingEngine.calculate_traffic_on_route` interface. The returned <a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a> could then be used to update `sdk.navigation.NavigatorInterface.traffic_on_route` to refresh the traffic on route visualization. Defaults to `false`. Gets the current state whether traffic conditions on route should be displayed during visual navigation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener">junctionViewLaneAssistanceListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span>  
Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive junction view lane assistance notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager">locationManager</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a></span>  
The location manager used by the navigator for map-matched location processing. Gets the location manager instance used by the navigator.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener">lowSpeedZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span>  
Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available *only* for Japan. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about low speed zones on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">maneuverArrowWidthFactor</a></span> <span class="signature">↔ double</span>  
A factor of <a href="sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth">VisualNavigator.measureDependentWidth</a> defining the width of the maneuver arrow. The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one. Gets the factor that multiplies width of the maneuver arrow defined by <a href="sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth">VisualNavigator.measureDependentWidth</a>. By default it is set to one.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions">maneuverNotificationOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span>  
Options used for maneuver notifications. Notifications are only available if a route is present. Gets the maneuver notification options.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener">maneuverViewLaneAssistanceListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span>  
Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive maneuver view lane assistance notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth">measureDependentWidth</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span>  
The `measureDependentWidth` that defines the route and maneuver arrows width. It is a dictionary that has keys that are <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s and values that are width in pixels at this <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">MapViewBase.pixelScale</a> before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with <a href="sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. For keys above the highest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. Only <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of `sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL` type are supported. <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of other unsupported types will be ignored. `measureDependentWidth` with a single entry is equivalent to use of the constant width value of this single entry for all <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. Empty `measureDependentWidth` is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then `measureDependentWidth` contains predefined values chosen to be optimal for different route classes.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener">milestoneStatusListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span>  
Object to receive notifications about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener">navigableLocationListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span>  
Object to receive notifications about the current location. It returns `null` when no listener is set by an user. Gets the listener that notifies current location updates.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener">offRoadDestinationReachedListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span>  
Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when the off-road destination has been reached.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener">offRoadProgressListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span>  
Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies about off-road progress.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener">postActionListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span>  
Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive post action notifications, such as a charge action at a charging station.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener">railwayCrossingWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span>  
Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about railway crossings on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener">realisticViewWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span>  
Object to receive notifications about junction views on the current road. Setting `null` value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about junction views on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions">realisticViewWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span>  
Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener">roadAttributesListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span>  
Object to receive notifications about attributes of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about attributes of the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener">roadSignWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span>  
Object to receive notifications about road signs on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about road signs on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions">roadSignWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span>  
Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>. Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener">roadTextsListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span>  
Object to receive notifications about the textual attributes of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about the textual attributes of the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-route">route</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span>  
The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>. If set, both route progress (<a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>) and route deviation (<a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect. Gets the route that is being navigated.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener">routeDeviationListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span>  
Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when deviation from the route is observed.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-routedraworder">routeDrawOrder</a></span> <span class="signature">↔ int</span>  
The draw order of the polylines representing the route. The draw order of the polylines representing the route. For more details see <a href="sdk-for-flutter-navigate-mapview-mappolyline-draworder">MapPolyline.drawOrder</a>. The default is 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-routedrawordertype">routeDrawOrderType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a></span>  
The draw order type of the polylines representing the route. The draw order type of the polylines representing the route. For more details see <a href="sdk-for-flutter-navigate-mapview-mappolyline-drawordertype">MapPolyline.drawOrderType</a>. The default is <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener">routeProgressListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span>  
Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a route progress change occurs.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener">safetyCameraWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span>  
Object to receive safety camera warner notifications. If a listener is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive safety camera warning notifications.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions">safetyCameraWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span>  
Safety camera warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner. Gets safety camera warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener">schoolZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span>  
Object to receive notifications about school zones on the current road. Setting `null` value to the listener will unset the listener. school zones on the current road. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about school zones on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions">schoolZoneWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span>  
School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>. Gets school zone warning options that allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener">speedLimitListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span>  
Object to receive notifications about the speed limit of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about the speed limit of the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener">speedWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span>  
Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions">speedWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span>  
Options used for the speed warning feature. Gets the speed warning options.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener">tollStopWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span>  
Object to receive information on the upcoming toll stop. Setting `null` value to the listener will unset the listener. This is a **beta release** of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets the listener to receive notifications about the the upcoming toll stop.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile" class="deprecated">trackingTransportProfile</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span>  
Defines the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a> can be defined with a <a href="sdk-for-flutter-navigate-transport-vehicleprofile-class" class="deprecated">VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">trackingTransportSpecification</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span>  
Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener">trafficMergeWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span>  
Object to receive notifications about merging traffic to the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about merging traffic to the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions">trafficMergeWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span>  
Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>. Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">trafficOnRoute</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span>  
Traffic information for the current route. This impacts `RouteProgress` updates as the duration of the `SectionProgress` might change. However, the remaining distance and the route geometry will remain unchanged. Gets the traffic information for the current route.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener">truckRestrictionsWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span>  
Object to receive notifications about truck restrictions on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about truck restrictions on the current road.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions">truckRestrictionsWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span>  
Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>. Gets truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine">warnerEngine</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-warner-warnerengine-class">WarnerEngine</a></span>  
Warner engine used by the navigator. This engine can be used to configure navigation warnings. Gets the warner engine used by the navigator.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters">calculateRemainingDistanceInMeters</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateRemainingDistanceInMeters-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ int?</span> </span>  
This method calculates the distance between the current position and given coordinates.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver">getManeuver</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getManeuver-param-index" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">index</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>?</span> </span>  
Returns maneuver at the given index.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile">getManeuverNotificationTimingOptionsWithTimingProfile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> </span>  
Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances">getWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> </span>  
Returns the warning notification distances for the requested warning type.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time a new location is available.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification">repeatLastManeuverNotification</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption">setCustomOption</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomOption-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-navigate-setCustomOption-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
This method sets custom options that controls navigator behavior.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile">setManeuverNotificationTimingOptionsWithTimingProfile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span>, </span><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Set timing option values for the combination of transport mode and timing profile.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances">setWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span>, </span><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Set the warning notification distances for the specified warning types.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">startRendering</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startRendering-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts visual navigation rendering.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">stopRendering</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops visual navigation rendering.

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-defaultroutemaneuverarrowmeasuredependentwidths">defaultRouteManeuverArrowMeasureDependentWidths</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span> </span>  
Retrieves a dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-getavailablelanguagesformaneuvernotifications">getAvailableLanguagesForManeuverNotifications</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span>\></span></span> </span>  
Returns the list of languages for maneuver notification currently available in the SDK.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
