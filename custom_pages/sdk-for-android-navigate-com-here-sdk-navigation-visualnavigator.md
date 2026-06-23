---
title: "VisualNavigator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VisualNavigator.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.VisualNavigator</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code>, <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VisualNavigator</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></span></div>
<div class="block"><p>This class provides all functionality of <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a>. In addition,
 it provides advanced rendering capabilities for a smooth navigation experience.
 This includes interpolation of location updates along a route during turn-by-turn navigation
 and during tracking mode. By default, suitable map view settings are automatically applied.
 For example, a predefined current location marker is rendered.
 Similar to <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, this class continuously reacts to new locations
 provided from a location source and acts as a <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a>.
 Note that the VisualNavigator takes control of the MapView's (maximum) frame rate when rendering,
 i.e., between <a href="sdk-for-android-navigate-index#startRendering(com.here.sdk.mapview.MapViewBase)"><code>startRendering(com.here.sdk.mapview.MapViewBase)</code></a> and <a href="sdk-for-android-navigate-index#stopRendering()"><code>stopRendering()</code></a> calls. It overwrites the MapView's frame
 rate when some camera behavior is set using the <a href="sdk-for-android-navigate-index#getGuidanceFrameRate()"><code>getGuidanceFrameRate()</code></a>. When no camera behavior
 is preset, the original MapView's frame rate (the value prior to the <a href="sdk-for-android-navigate-index#startRendering(com.here.sdk.mapview.MapViewBase)"><code>startRendering(com.here.sdk.mapview.MapViewBase)</code></a> call) will
 be used. While the VisualNavigator is rendering, direct changes in the MapView's frame rate can
 lead to unexpected behavior and therefore should be avoided.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">VisualNavigator</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">VisualNavigator</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.NavigatorInterface)">VisualNavigator</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class using provided instance of <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> as source of data.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.navigation.NavigatorInterface)">VisualNavigator</a><wbr/>(<a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class using provided instance of <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> as source of data.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">calculateRemainingDistanceInMeters</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method calculates the distance between the current position and given coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#defaultRouteManeuverArrowMeasureDependentWidths()">defaultRouteManeuverArrowMeasureDependentWidths</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getAvailableLanguagesForManeuverNotifications()">getAvailableLanguagesForManeuverNotifications</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the list of languages for maneuver notification currently available in the SDK.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBorderCrossingWarningListener()">getBorderCrossingWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about border crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBorderCrossingWarningOptions()">getBorderCrossingWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getCameraBehavior()">getCameraBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set camera behavior.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getColors()">getColors</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an object containing colors used to render route progress and maneuver arrow visualization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getCurrentSituationLaneAssistanceViewListener()">getCurrentSituationLaneAssistanceViewListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive current situation lane assistance view notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getCustomLocationIndicator()">getCustomLocationIndicator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set <code>LocationIndicator</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDangerZoneWarningListener()">getDangerZoneWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive current danger zones notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDebugGpxFilePath()">getDebugGpxFilePath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the path of the GPX file, is any available, currently being displayed on the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDestinationReachedListener()">getDestinationReachedListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notify when the destination has been reached.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getEnvironmentalZoneWarningListener()">getEnvironmentalZoneWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive current environmental zones notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getEventTextListener()">getEventTextListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies when a text notification is available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getEventTextOptions()">getEventTextOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text notification options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getGuidanceFrameRate()">getGuidanceFrameRate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frame rate used during guidance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getInterpolatedLocationListener()">getInterpolatedLocationListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that receives interpolated locations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getJunctionViewLaneAssistanceListener()">getJunctionViewLaneAssistanceListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive junction view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLocationManager()">getLocationManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the location manager instance used by the navigator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLowSpeedZoneWarningListener()">getLowSpeedZoneWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about low speed zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maneuver" title="class in com.here.sdk.routing">Maneuver</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuver(int)">getManeuver</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns maneuver at the given index.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuverArrowWidthFactor()">getManeuverArrowWidthFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the factor that multiplies width of the maneuver arrow defined by
 <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuverNotificationOptions()">getManeuverNotificationOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maneuver notification options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">getManeuverNotificationTimingOptions</a><wbr/>(<a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuverViewLaneAssistanceListener()">getManeuverViewLaneAssistanceListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive maneuver view lane assistance notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getMeasureDependentWidth()">getMeasureDependentWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent polyline and maneuver arrow width in pixels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getMilestoneStatusListener()">getMilestoneStatusListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getNavigableLocationListener()">getNavigableLocationListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies current location updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getOffRoadDestinationReachedListener()">getOffRoadDestinationReachedListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies when the off-road destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getOffRoadProgressListener()">getOffRoadProgressListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies about off-road progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPostActionListener()">getPostActionListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive post action notifications, such as a charge action at a charging station.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRailwayCrossingWarningListener()">getRailwayCrossingWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about railway crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRealisticViewWarningListener()">getRealisticViewWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about junction views on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRealisticViewWarningOptions()">getRealisticViewWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadAttributesListener()">getRoadAttributesListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive notifications about attributes of the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadSignWarningListener()">getRoadSignWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about road signs on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadSignWarningOptions()">getRoadSignWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadTextsListener()">getRoadTextsListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive notifications about the textual attributes of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoute()">getRoute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the route that is being navigated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRouteDeviationListener()">getRouteDeviationListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies when deviation from the route is observed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRouteDrawOrder()">getRouteDrawOrder</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The draw order of the polylines representing the route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRouteDrawOrderType()">getRouteDrawOrderType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The draw order type of the polylines representing the route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRouteProgressListener()">getRouteProgressListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener that notifies when a route progress change occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSafetyCameraWarningListener()">getSafetyCameraWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive safety camera warning notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSafetyCameraWarningOptions()">getSafetyCameraWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSchoolZoneWarningListener()">getSchoolZoneWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about school zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSchoolZoneWarningOptions()">getSchoolZoneWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSpeedLimitListener()">getSpeedLimitListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive notifications about the speed limit of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSpeedWarningListener()">getSpeedWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSpeedWarningOptions()">getSpeedWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the speed warning options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTollStopWarningListener()">getTollStopWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about
 the the upcoming toll stop.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrackingTransportProfile()">getTrackingTransportProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrackingTransportSpecification()">getTrackingTransportSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficMergeWarningListener()">getTrafficMergeWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener to receive notifications about
 merging traffic to the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficMergeWarningOptions()">getTrafficMergeWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficOnRoute()">getTrafficOnRoute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the traffic information for the current route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTruckRestrictionsWarningListener()">getTruckRestrictionsWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the listener  to receive notifications about
 truck restrictions on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTruckRestrictionsWarningOptions()">getTruckRestrictionsWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getWarnerEngine()">getWarnerEngine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the warner engine used by the navigator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">getWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the warning notification distances for the requested warning type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isDebugModeEnabled()">isDebugModeEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current debug mode state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isDynamicFrameRateEnabled()">isDynamicFrameRateEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Controls whether the number of map updates is dynamically calculated based on
 the current zoom level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isEnableTunnelExtrapolation()">isEnableTunnelExtrapolation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isExtrapolationEnabled()">isExtrapolationEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state of the position extrapolation logic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isLocationAccuracyVisualized()">isLocationAccuracyVisualized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a boolean indicating if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is rendered or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isManeuverArrowsVisible()">isManeuverArrowsVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state of maneuver arrow rendering during visual navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isOffRoadDestinationVisible()">isOffRoadDestinationVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state of off-road destination visualization during visual navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isPassthroughWaypointsHandlingEnabled()">isPassthroughWaypointsHandlingEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isRendering()">isRendering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a value indicating whether visual navigation rendering is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isRouteProgressVisible()">isRouteProgressVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state of route progress during visual navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isRouteVisible()">isRouteVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state of route rendering during visual navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isTrafficOnRouteVisible()">isTrafficOnRouteVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current state whether traffic conditions on route should be displayed during visual navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called each time a new location is available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#repeatLastManeuverNotification()">repeatLastManeuverNotification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">setBorderCrossingWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about border crossings on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">setBorderCrossingWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setCameraBehavior(com.here.sdk.navigation.CameraBehavior)">setCameraBehavior</a><wbr/>(<a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets how the VisualNavigator handles the camera.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setColors(com.here.sdk.navigation.VisualNavigatorColors)">setColors</a><wbr/>(<a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets an object containing colors used to render route progress and maneuver arrow visualization.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">setCurrentSituationLaneAssistanceViewListener</a><wbr/>(<a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive current situation lane assistance view notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setCustomLocationIndicator(com.here.sdk.mapview.LocationIndicator)">setCustomLocationIndicator</a><wbr/>(<a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>, so that <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> uses the provided one instead
 of the default.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method sets custom options that controls navigator behavior.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">setDangerZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive current danger zones notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDebugGpxFilePath(java.lang.String)">setDebugGpxFilePath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the path of a GPX file to be displayed on the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDebugModeEnabled(boolean)">setDebugModeEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to enable debug mode or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">setDestinationReachedListener</a><wbr/>(<a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notify when the destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDynamicFrameRateEnabled(boolean)">setDynamicFrameRateEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Controls whether the number of map updates is dynamically calculated based on
 the current zoom level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setEnableTunnelExtrapolation(boolean)">setEnableTunnelExtrapolation</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to <code>true</code> to enable tunnel extrapolation, set to <code>false</code> to disable tunnel extrapolation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">setEnvironmentalZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive current environmental zones notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setEventTextListener(com.here.sdk.navigation.EventTextListener)">setEventTextListener</a><wbr/>(<a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies when a text notification is available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">setEventTextOptions</a><wbr/>(<a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the text notification options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setExtrapolationEnabled(boolean)">setExtrapolationEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to enable or disable the position extrapolation logic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setGuidanceFrameRate(int)">setGuidanceFrameRate</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frame rate used during guidance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setInterpolatedLocationListener(com.here.sdk.navigation.InterpolatedLocationListener)">setInterpolatedLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that receives interpolated locations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">setJunctionViewLaneAssistanceListener</a><wbr/>(<a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive junction view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setLocationAccuracyVisualized(boolean)">setLocationAccuracyVisualized</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">setLowSpeedZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about low speed zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverArrowsVisible(boolean)">setManeuverArrowsVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to perform maneuver arrow rendering during visual navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverArrowWidthFactor(double)">setManeuverArrowWidthFactor</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the factor that multiplies the width of the maneuver arrow defined by the
 <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">setManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the maneuver notification options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">setManeuverNotificationTimingOptions</a><wbr/>(<a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile,
 <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set timing option values for the combination of transport mode and timing profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">setManeuverViewLaneAssistanceListener</a><wbr/>(<a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive maneuver view lane assistance notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setMeasureDependentWidth(java.util.Map)">setMeasureDependentWidth</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent route and maneuver arrows width in pixels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">setMilestoneStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">setNavigableLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies current location updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">setOffRoadDestinationReachedListener</a><wbr/>(<a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies when the off-road destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setOffRoadDestinationVisible(boolean)">setOffRoadDestinationVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to show a dashed line between the map-matched and the original destination
 which is off-road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">setOffRoadProgressListener</a><wbr/>(<a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies about off-road progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setPassthroughWaypointsHandlingEnabled(boolean)">setPassthroughWaypointsHandlingEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to <code>true</code> enables handling of passthrough waypoints, set to <code>false</code> disables handling of passthrough waypoints.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setPostActionListener(com.here.sdk.navigation.PostActionListener)">setPostActionListener</a><wbr/>(<a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive post action notifications, such as a charge action at a charging station.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">setRailwayCrossingWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about railway crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">setRealisticViewWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about junction views on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">setRealisticViewWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">setRoadAttributesListener</a><wbr/>(<a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive notifications about attributes of the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">setRoadSignWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about road signs on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">setRoadSignWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">setRoadTextsListener</a><wbr/>(<a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive notifications about the textual attributes of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoute(com.here.sdk.routing.Route)">setRoute</a><wbr/>(<a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the route to navigate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">setRouteDeviationListener</a><wbr/>(<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies when deviation from the route is observed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteDrawOrder(int)">setRouteDrawOrder</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The draw order of the polylines representing the route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteDrawOrderType(com.here.sdk.mapview.DrawOrderType)">setRouteDrawOrderType</a><wbr/>(<a href="sdk-for-android-navigate-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The draw order type of the polylines representing the route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">setRouteProgressListener</a><wbr/>(<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener that notifies when a route progress change occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteProgressVisible(boolean)">setRouteProgressVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to perform route progress coloring ("eat-up") during visual navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRouteVisible(boolean)">setRouteVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to perform route rendering during visual navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">setSafetyCameraWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive safety camera warning notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">setSafetyCameraWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">setSchoolZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about school zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">setSchoolZoneWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">setSpeedLimitListener</a><wbr/>(<a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive notifications about the speed limit of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">setSpeedWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">setSpeedWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the speed warning options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">setTollStopWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about
 the upcoming toll stop.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">setTrackingTransportProfile</a><wbr/>(<a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">setTrackingTransportSpecification</a><wbr/>(<a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">setTrafficMergeWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener to receive notifications about
 merging traffic to the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">setTrafficMergeWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">setTrafficOnRoute</a><wbr/>(<a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the traffic information for the current route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTrafficOnRouteVisible(boolean)">setTrafficOnRouteVisible</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization is enabled
 during visual navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">setTruckRestrictionsWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the listener  to receive notifications about
 truck restrictions on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">setTruckRestrictionsWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">setWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the warning notification distances for the specified warning types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#startRendering(com.here.sdk.mapview.MapViewBase)">startRendering</a><wbr/>(<a href="sdk-for-android-navigate-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts visual navigation rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#stopRendering()">stopRendering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops visual navigation rendering.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>VisualNavigator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VisualNavigator</span>()
                throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> when operation fails.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>VisualNavigator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> when operation fails.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.NavigatorInterface)">
<h3>VisualNavigator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span>
                throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class using provided instance of <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> as source of data.
 </p><p><strong>Note:</strong> The <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> implements the <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> interface and forwards
 all calls to the underlying <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> instance. When multiple <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a>
 instances share the same <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> instance, method calls on this common instance
 will overwrite changes made by another, which may lead to unexpected behavior.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>navigator</code> - <p>A NavigatorInterface implementation instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> when operation fails.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.navigation.NavigatorInterface)">
<h3>VisualNavigator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VisualNavigator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span>
                throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class using provided instance of <a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> as source of data.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dd><code>navigator</code> - <p>A NavigatorInterface implementation instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> when operation fails.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getAvailableLanguagesForManeuverNotifications()">
<h3>getAvailableLanguagesForManeuverNotifications</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a>&gt;</span> <span class="element-name">getAvailableLanguagesForManeuverNotifications</span>()</div>
<div class="block"><p>Returns the list of languages for maneuver notification currently available in the SDK.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>the list of languages for maneuver notification currently available in the SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startRendering(com.here.sdk.mapview.MapViewBase)">
<h3>startRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startRendering</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Starts visual navigation rendering.
 A preconfigured current location marker is shown as soon as a location is received.
 The marker is chosen according to the transport mode specified in the route. If no route is
 present, the marker is chosen based on the <a href="sdk-for-android-navigate-navigatorinterface#getTrackingTransportSpecification()"><code>NavigatorInterface.getTrackingTransportSpecification()</code></a> property.
 Calling startRendering() changes the <a href="sdk-for-android-navigate-mapcamera#getPrincipalPoint()"><code>MapCamera.getPrincipalPoint()</code></a> property so that the current
 position indicator is equal to the value from <a href="sdk-for-android-navigate-camerabehavior#getNormalizedPrincipalPoint()"><code>CameraBehavior.getNormalizedPrincipalPoint()</code></a>,
 in which by default places the principal point slightly at the bottom of the mapview. It is
 restored to its original value when stopRendering() is called.
 <strong>Note:</strong> When rendering is started again for a new map view instance, rendering
 is automatically stopped on the previous map view instance. Also note that
 the <a href="sdk-for-android-navigate-mapviewbase#getFrameRate()"><code>MapViewBase.getFrameRate()</code></a> can be lowered to reduce CPU usage, to adjust for tradeoffs
 between rendering smoothness versus battery consumption.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The map view on which visual navigation will take place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stopRendering()">
<h3>stopRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stopRendering</span>()</div>
<div class="block"><p>Stops visual navigation rendering. This removes the current location marker. Other
 settings, like map orientation or camera distance, which may have been altered during rendering
 are no longer updated.</p></div>
</section>
</li>
<li>
<section class="detail" id="defaultRouteManeuverArrowMeasureDependentWidths()">
<h3>defaultRouteManeuverArrowMeasureDependentWidths</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</span> <span class="element-name">defaultRouteManeuverArrowMeasureDependentWidths</span>()</div>
<div class="block"><p>Retrieves a dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraBehavior()">
<h3>getCameraBehavior</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span> <span class="element-name">getCameraBehavior</span>()</div>
<div class="block"><p>Gets the currently set camera behavior.
 </p><p>Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
 the current location and keeps the last active camera state, i.e., current zoom and tilt.
 Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
 the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
 zoomed by the user.
 The default value is an instance of <a href="sdk-for-android-navigate-fixedcamerabehavior" title="class in com.here.sdk.navigation"><code>FixedCameraBehavior</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera behavior which defines how the <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> handles the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraBehavior(com.here.sdk.navigation.CameraBehavior)">
<h3>setCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBehavior</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a> value)</span></div>
<div class="block"><p>Sets how the VisualNavigator handles the camera.
 </p><p>Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
 the current location and keeps the last active camera state, i.e., current zoom and tilt.
 Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
 the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
 zoomed by the user.
 The default value is an instance of <a href="sdk-for-android-navigate-fixedcamerabehavior" title="class in com.here.sdk.navigation"><code>FixedCameraBehavior</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera behavior which defines how the <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> handles the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRouteVisible()">
<h3>isRouteVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRouteVisible</span>()</div>
<div class="block"><p>Gets the current state of route rendering during visual navigation.
 </p><p>When enabled, the set <code>Route</code> will be rendered as a <code>MapPolyline</code> together with <code>MapArrow</code> items that
 indicate the next turns. By default, it is enabled.
 When disabled, <code>MapArrow</code> items are still rendered. To hide arrows, use <code>VisualNavigatorColors</code> with
 transparent color.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>Route</code> visibility which defines whether to perform route rendering during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteVisible(boolean)">
<h3>setRouteVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to perform route rendering during visual navigation.
 </p><p>When enabled, the set <code>Route</code> will be rendered as a <code>MapPolyline</code> together with <code>MapArrow</code> items that
 indicate the next turns. By default, it is enabled.
 When disabled, <code>MapArrow</code> items are still rendered. To hide arrows, use <code>VisualNavigatorColors</code> with
 transparent color.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><code>Route</code> visibility which defines whether to perform route rendering during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRouteProgressVisible()">
<h3>isRouteProgressVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRouteProgressVisible</span>()</div>
<div class="block"><p>Gets the current state of route progress during visual navigation.
 </p><p>By default, it is enabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>RouteProgress</code> visibility which defines whether to perform route progress coloring ("eat-up") during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteProgressVisible(boolean)">
<h3>setRouteProgressVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to perform route progress coloring ("eat-up") during visual navigation.
 </p><p>By default, it is enabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p><code>RouteProgress</code> visibility which defines whether to perform route progress coloring ("eat-up") during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isManeuverArrowsVisible()">
<h3>isManeuverArrowsVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverArrowsVisible</span>()</div>
<div class="block"><p>Gets the current state of maneuver arrow rendering during visual navigation.
 </p><p>By default, it is enabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverArrowsVisible(boolean)">
<h3>setManeuverArrowsVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowsVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to perform maneuver arrow rendering during visual navigation.
 </p><p>By default, it is enabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOffRoadDestinationVisible()">
<h3>isOffRoadDestinationVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOffRoadDestinationVisible</span>()</div>
<div class="block"><p>Gets the current state of off-road destination visualization during visual navigation.
 </p><p><strong>Note:</strong> The dashed line will be drawn only if the original destination is off-road.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination
     which is off-road. By default it is enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOffRoadDestinationVisible(boolean)">
<h3>setOffRoadDestinationVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadDestinationVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to show a dashed line between the map-matched and the original destination
 which is off-road.
 </p><p><strong>Note:</strong> The dashed line will be drawn only if the original destination is off-road.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination
     which is off-road. By default it is enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTrafficOnRouteVisible()">
<h3>isTrafficOnRouteVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTrafficOnRouteVisible</span>()</div>
<div class="block"><p>Gets the current state whether traffic conditions on route should be displayed during visual navigation.
 </p><p>When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
 Colors used for this visualization are defined in <a href="sdk-for-android-navigate-visualnavigatorcolors#getTrafficOnRouteColors()"><code>VisualNavigatorColors.getTrafficOnRouteColors()</code></a>.
 The presented traffic information is either set by the user via <a href="sdk-for-android-navigate-navigatorinterface#getTrafficOnRoute()"><code>NavigatorInterface.getTrafficOnRoute()</code></a> or
 is generated from historical traffic data stored in the map.
 <strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
 through the [sdk.routing.RoutingEngine.calculate_traffic_on_route] interface. The returned <a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing"><code>TrafficOnRoute</code></a>
 could then be used to update [sdk.navigation.NavigatorInterface.traffic_on_route] to refresh the traffic on route visualization.
 Defaults to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
     is enabled during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficOnRouteVisible(boolean)">
<h3>setTrafficOnRouteVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRouteVisible</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization is enabled
 during visual navigation.
 </p><p>When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
 Colors used for this visualization are defined in <a href="sdk-for-android-navigate-visualnavigatorcolors#getTrafficOnRouteColors()"><code>VisualNavigatorColors.getTrafficOnRouteColors()</code></a>.
 The presented traffic information is either set by the user via <a href="sdk-for-android-navigate-navigatorinterface#getTrafficOnRoute()"><code>NavigatorInterface.getTrafficOnRoute()</code></a> or
 is generated from historical traffic data stored in the map.
 <strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
 through the [sdk.routing.RoutingEngine.calculate_traffic_on_route] interface. The returned <a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing"><code>TrafficOnRoute</code></a>
 could then be used to update [sdk.navigation.NavigatorInterface.traffic_on_route] to refresh the traffic on route visualization.
 Defaults to <code>false</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
     is enabled during visual navigation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomLocationIndicator()">
<h3>getCustomLocationIndicator</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a></span> <span class="element-name">getCustomLocationIndicator</span>()</div>
<div class="block"><p>Gets the currently set <code>LocationIndicator</code>.
 </p><p>If set, the user is responsible for adding and removing the object to/from the mapview.
 It is important to stop sending location updates to the provided <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>, since
 <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> will control its position when rendering is active, i.e., between startRendering() and
 stopRendering() calls. By default this property is <code>null</code>,
 which means the default indicator is used, and <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> automatically adds and removes it to/from
 the mapview upon startRendering() and stopRendering() calls.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Custom location indicator <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> which <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> uses instead of the default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomLocationIndicator(com.here.sdk.mapview.LocationIndicator)">
<h3>setCustomLocationIndicator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomLocationIndicator</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview">LocationIndicator</a> value)</span></div>
<div class="block"><p>Sets a custom <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>, so that <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> uses the provided one instead
 of the default.
 </p><p>If set, the user is responsible for adding and removing the object to/from the mapview.
 It is important to stop sending location updates to the provided <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>, since
 <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> will control its position when rendering is active, i.e., between startRendering() and
 stopRendering() calls. By default this property is <code>null</code>,
 which means the default indicator is used, and <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> automatically adds and removes it to/from
 the mapview upon startRendering() and stopRendering() calls.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Custom location indicator <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> which <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> uses instead of the default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInterpolatedLocationListener()">
<h3>getInterpolatedLocationListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a></span> <span class="element-name">getInterpolatedLocationListener</span>()</div>
<div class="block"><p>Gets the listener that receives interpolated locations.
 For example, to pan a second instance of a
 <a href="sdk-for-android-navigate-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a> or move additional markers smoothly. The map-matched locations are
 used if available, otherwise the non-map-matched ones are used instead.
 </p><p>For example, to pan a second instance of a <a href="sdk-for-android-navigate-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a> or move additional markers smoothly.
 The map-matched locations are used if available, otherwise the non-map-matched ones are used instead.
 Defaults to <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive interpolated locations.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInterpolatedLocationListener(com.here.sdk.navigation.InterpolatedLocationListener)">
<h3>setInterpolatedLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInterpolatedLocationListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-interpolatedlocationlistener" title="interface in com.here.sdk.navigation">InterpolatedLocationListener</a> value)</span></div>
<div class="block"><p>Sets the listener that receives interpolated locations.
 </p><p>For example, to pan a second instance of a <a href="sdk-for-android-navigate-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a> or move additional markers smoothly.
 The map-matched locations are used if available, otherwise the non-map-matched ones are used instead.
 Defaults to <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive interpolated locations.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRendering()">
<h3>isRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRendering</span>()</div>
<div class="block"><p>Returns a value indicating whether visual navigation rendering is enabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Returns a value indicating whether visual navigation rendering is enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColors()">
<h3>getColors</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">getColors</span>()</div>
<div class="block"><p>Gets an object containing colors used to render route progress and maneuver arrow visualization.
 </p><p>Setting a new instance overwrites the default color settings as specified in <code>VisualNavigatorColors</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object containing colors used to render route progress and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setColors(com.here.sdk.navigation.VisualNavigatorColors)">
<h3>setColors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColors</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a> value)</span></div>
<div class="block"><p>Sets an object containing colors used to render route progress and maneuver arrow visualization.
 </p><p>Setting a new instance overwrites the default color settings as specified in <code>VisualNavigatorColors</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object containing colors used to render route progress and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMeasureDependentWidth()">
<h3>getMeasureDependentWidth</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</span> <span class="element-name">getMeasureDependentWidth</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent polyline and maneuver arrow width in pixels.
 </p><p>It is a dictionary that has keys that are <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s and values
 that are width in pixels at this <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.
 This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-android-navigate-mapviewbase#getPixelScale()"><code>MapViewBase.getPixelScale()</code></a>
 before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
 <code>setManeuverArrowWidthFactor</code>; which by default equals one.
 The function defined by a dictionary is linearly interpolated between each successive pair of data points.
 For keys below the lowest <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>, its corresponding value width is used.
 For keys above the highest <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>, its corresponding value width is used.
 Only <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> of [sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL] type are supported.
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> of other unsupported types will be ignored.
 <code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
 value of this single entry for all <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.
 Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
 The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
 If route and maneuver arrows were not configured with this property,
 then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMeasureDependentWidth(java.util.Map)">
<h3>setMeasureDependentWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMeasureDependentWidth</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent route and maneuver arrows width in pixels.
 </p><p>It is a dictionary that has keys that are <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s and values
 that are width in pixels at this <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.
 This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-android-navigate-mapviewbase#getPixelScale()"><code>MapViewBase.getPixelScale()</code></a>
 before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
 <code>setManeuverArrowWidthFactor</code>; which by default equals one.
 The function defined by a dictionary is linearly interpolated between each successive pair of data points.
 For keys below the lowest <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>, its corresponding value width is used.
 For keys above the highest <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>, its corresponding value width is used.
 Only <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> of [sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL] type are supported.
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> of other unsupported types will be ignored.
 <code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
 value of this single entry for all <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>s.
 Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
 The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
 If route and maneuver arrows were not configured with this property,
 then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverArrowWidthFactor()">
<h3>getManeuverArrowWidthFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getManeuverArrowWidthFactor</span>()</div>
<div class="block"><p>Gets the factor that multiplies width of the maneuver arrow defined by
 <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a>. By default it is set to one.
 </p><p>The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A factor of <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a> defining the width of the maneuver arrow.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverArrowWidthFactor(double)">
<h3>setManeuverArrowWidthFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowWidthFactor</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the factor that multiplies the width of the maneuver arrow defined by the
 <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a>.
 </p><p>The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A factor of <a href="sdk-for-android-navigate-index#getMeasureDependentWidth()"><code>getMeasureDependentWidth()</code></a> defining the width of the maneuver arrow.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExtrapolationEnabled()">
<h3>isExtrapolationEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExtrapolationEnabled</span>()</div>
<div class="block"><p>Gets the current state of the position extrapolation logic.
 </p><p>The predicted location follows the geometry of the route (or road) ahead.
 By default it is enabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines whether the position extrapolation logic is enabled or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExtrapolationEnabled(boolean)">
<h3>setExtrapolationEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExtrapolationEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to enable or disable the position extrapolation logic. By default enabled.
 </p><p>The predicted location follows the geometry of the route (or road) ahead.
 By default it is enabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether the position extrapolation logic is enabled or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDebugGpxFilePath()">
<h3>getDebugGpxFilePath</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDebugGpxFilePath</span>()</div>
<div class="block"><p>Gets the path of the GPX file, is any available, currently being displayed on the map.
 </p><p><strong>Note:</strong> This API should be used for debugging purposes only.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Show the contents of a GPX file on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDebugGpxFilePath(java.lang.String)">
<h3>setDebugGpxFilePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDebugGpxFilePath</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets the path of a GPX file to be displayed on the map. Setting <code>null</code> removes it from
 the map.
 </p><p><strong>Note:</strong> This API should be used for debugging purposes only.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Show the contents of a GPX file on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDebugModeEnabled()">
<h3>isDebugModeEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDebugModeEnabled</span>()</div>
<div class="block"><p>Gets the current debug mode state.
 <ul>
<li>A semi-transparent location marker indicating the map-matched location.</li>
<li>A gray, semi-transparent location marker indicating the raw (or original) input location.</li>
<li>A red polyline indicating the most probable path.</li>
<li>A SVG overlay, on the middle-left of the screen, showing the following:
 <ul>
<li>IN - Input location: coordinates [bearing] [speed] [accuracy]</li>
<li>RM - Route-matched location: coordinates bearing (distance-to-raw-location)</li>
<li>MM - Map-Matched location: coordinates bearing (distance-to-raw-location)</li>
<li>RM-MM - distance-between-route-and-map-matched-locations</li>
<li>RP - Route progress: remaining-duration remaining-distance</li>
<li>SP - Section progress: section-index/sections-count remaining-duration remaining-distance</li>
<li>MP - Maneuver progress: maneuver-index remaining-duration remaining-distance</li>
<li>CPU - CPU usage: cpu-usage current-date-time</li>
<li>MS - Milestone status: section-index MISSED|REACHED when</li>
<li>RD - Route deviation: last-traveled-section-index last-traveled-section-distance when</li>
<li>FPS - Frames per second: frames-per-second</li>
</ul>
</li>
</ul>
</p><p>Fields between brackets ([]'s) are omitted if not available.
 </p><p>Example:
 <pre>
 IN: 53.96880,14.77903 167° 8m/s
 RM: 53.96880,14.77903 167° (0.0m)
 MM: 53.96879,14.77903 167° (0.5m)
 RM-MM: 0.5m
 RP: 49h0m3s 4302km
 SP: 0/16 1h2m20s 58km
 MP: 1 5s 25m
 CPU: 7% 2024-01-01 13:21:59
 MS: 1 REACHED 12:34:22
 RD: 2 345m 11:13:55
 FPS: 30.0
 </pre>
</p><p><strong>Note:</strong> This API should be used for debugging purposes only.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>When enabled, it shows useful information for debugging purposes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDebugModeEnabled(boolean)">
<h3>setDebugModeEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDebugModeEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to enable debug mode or not.
 <ul>
<li>A semi-transparent location marker indicating the map-matched location.</li>
<li>A gray, semi-transparent location marker indicating the raw (or original) input location.</li>
<li>A red polyline indicating the most probable path.</li>
<li>A SVG overlay, on the middle-left of the screen, showing the following:
 <ul>
<li>IN - Input location: coordinates [bearing] [speed] [accuracy]</li>
<li>RM - Route-matched location: coordinates bearing (distance-to-raw-location)</li>
<li>MM - Map-Matched location: coordinates bearing (distance-to-raw-location)</li>
<li>RM-MM - distance-between-route-and-map-matched-locations</li>
<li>RP - Route progress: remaining-duration remaining-distance</li>
<li>SP - Section progress: section-index/sections-count remaining-duration remaining-distance</li>
<li>MP - Maneuver progress: maneuver-index remaining-duration remaining-distance</li>
<li>CPU - CPU usage: cpu-usage current-date-time</li>
<li>MS - Milestone status: section-index MISSED|REACHED when</li>
<li>RD - Route deviation: last-traveled-section-index last-traveled-section-distance when</li>
<li>FPS - Frames per second: frames-per-second</li>
</ul>
</li>
</ul>
</p><p>Fields between brackets ([]'s) are omitted if not available.
 </p><p>Example:
 <pre>
 IN: 53.96880,14.77903 167° 8m/s
 RM: 53.96880,14.77903 167° (0.0m)
 MM: 53.96879,14.77903 167° (0.5m)
 RM-MM: 0.5m
 RP: 49h0m3s 4302km
 SP: 0/16 1h2m20s 58km
 MP: 1 5s 25m
 CPU: 7% 2024-01-01 13:21:59
 MS: 1 REACHED 12:34:22
 RD: 2 345m 11:13:55
 FPS: 30.0
 </pre>
</p><p><strong>Note:</strong> This API should be used for debugging purposes only.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>When enabled, it shows useful information for debugging purposes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocationAccuracyVisualized()">
<h3>isLocationAccuracyVisualized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLocationAccuracyVisualized</span>()</div>
<div class="block"><p>Gets a boolean indicating if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is rendered or not.
 </p><p>Does not affect halo accuracy indicator of the <a href="sdk-for-android-navigate-index#getCustomLocationIndicator()"><code>getCustomLocationIndicator()</code></a>.
 If <a href="sdk-for-android-navigate-index#getCustomLocationIndicator()"><code>getCustomLocationIndicator()</code></a> is set, then its halo accuracy indicator can be controlled
 using <a href="sdk-for-android-navigate-locationindicator#isAccuracyVisualized()"><code>LocationIndicator.isAccuracyVisualized()</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Controls if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is rendered or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocationAccuracyVisualized(boolean)">
<h3>setLocationAccuracyVisualized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocationAccuracyVisualized</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>.
 </p><p>Does not affect halo accuracy indicator of the <a href="sdk-for-android-navigate-index#getCustomLocationIndicator()"><code>getCustomLocationIndicator()</code></a>.
 If <a href="sdk-for-android-navigate-index#getCustomLocationIndicator()"><code>getCustomLocationIndicator()</code></a> is set, then its halo accuracy indicator can be controlled
 using <a href="sdk-for-android-navigate-locationindicator#isAccuracyVisualized()"><code>LocationIndicator.isAccuracyVisualized()</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Controls if the halo accuracy visualization of the default <a href="sdk-for-android-navigate-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is rendered or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDynamicFrameRateEnabled()">
<h3>isDynamicFrameRateEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDynamicFrameRateEnabled</span>()</div>
<div class="block"><p>Controls whether the number of map updates is dynamically calculated based on
 the current zoom level. If the zoom level is low, i.e., the camera target distance is high,
 updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will
 happen less frequent. It is on by default.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Flag used to enable or disable the dynamic frame rate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDynamicFrameRateEnabled(boolean)">
<h3>setDynamicFrameRateEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDynamicFrameRateEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Controls whether the number of map updates is dynamically calculated based on
 the current zoom level. If the zoom level is low, i.e., the camera target distance is high,
 updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will
 happen less frequent. It is on by default.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Flag used to enable or disable the dynamic frame rate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGuidanceFrameRate()">
<h3>getGuidanceFrameRate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGuidanceFrameRate</span>()</div>
<div class="block"><p>Frame rate used during guidance.
 Default is 30fps.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Frame rate used during guidance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuidanceFrameRate(int)">
<h3>setGuidanceFrameRate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGuidanceFrameRate</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Frame rate used during guidance.
 Default is 30fps.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Frame rate used during guidance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteDrawOrder()">
<h3>getRouteDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getRouteDrawOrder</span>()</div>
<div class="block"><p>The draw order of the polylines representing the route. For more details see
 <a href="sdk-for-android-navigate-mappolyline#getDrawOrder()"><code>MapPolyline.getDrawOrder()</code></a>.
 The default is 0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order of the polylines representing the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteDrawOrder(int)">
<h3>setRouteDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDrawOrder</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>The draw order of the polylines representing the route. For more details see
 <a href="sdk-for-android-navigate-mappolyline#getDrawOrder()"><code>MapPolyline.getDrawOrder()</code></a>.
 The default is 0.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of the polylines representing the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteDrawOrderType()">
<h3>getRouteDrawOrderType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></span> <span class="element-name">getRouteDrawOrderType</span>()</div>
<div class="block"><p>The draw order type of the polylines representing the route. For more details
 see <a href="sdk-for-android-navigate-mappolyline#getDrawOrderType()"><code>MapPolyline.getDrawOrderType()</code></a>.
 The default is <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order type of the polylines representing the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteDrawOrderType(com.here.sdk.mapview.DrawOrderType)">
<h3>setRouteDrawOrderType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDrawOrderType</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</span></div>
<div class="block"><p>The draw order type of the polylines representing the route. For more details
 see <a href="sdk-for-android-navigate-mappolyline#getDrawOrderType()"><code>MapPolyline.getDrawOrderType()</code></a>.
 The default is <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order type of the polylines representing the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuver(int)">
<h3>getManeuver</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span class="element-name">getManeuver</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block"><p>Returns maneuver at the given index.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuver(int)">getManeuver</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - <p>The index of maneuver requested.</p></dd>
<dt>Returns:</dt>
<dd><p>The maneuver if it exists or otherwise <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">
<h3>getManeuverNotificationTimingOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></span> <span class="element-name">getManeuverNotificationTimingOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</span></div>
<div class="block"><p>Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
 The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes
 of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function
 for the same combination of transport mode and timing profile.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">getManeuverNotificationTimingOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dt>Returns:</dt>
<dd><p>The timing options with default values.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">
<h3>setManeuverNotificationTimingOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setManeuverNotificationTimingOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile,
 @NonNull
 <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</span></div>
<div class="block"><p>Set timing option values for the combination of transport mode and timing profile.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">setManeuverNotificationTimingOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dd><code>options</code> - <p>The timing options.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when options has invalid value, see <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation"><code>ManeuverNotificationTimingOptions</code></a> for
     more details about options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">
<h3>getWarningNotificationDistances</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span></div>
<div class="block"><p>Returns the warning notification distances for the requested warning type. The return value can be used as the
 base for configuring warning notification distances. Configure the relevant attributes of this object according
 to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
 warning type and the modified warning notification distances object.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">getWarningNotificationDistances</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the notification distances will be returned.</p></dd>
<dt>Returns:</dt>
<dd><p>The notification distances for the given warning type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setWarningNotificationDistances</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 @NonNull
 <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div class="block"><p>Set the warning notification distances for the specified warning types.
 <strong>Note:</strong> The warning notification distances are set for most warners.
 This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
 Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code>TimingProfile</code>.
 If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
 Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code>TimingProfile</code>.
 Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
 seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">setWarningNotificationDistances</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the warning notification distances will be set.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be set for the specified warning types.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when the warning_type is [WarningType.SCHOOL_ZONE] or the options have invalid values,
     see <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> for more details about warning notification distances.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="repeatLastManeuverNotification()">
<h3>repeatLastManeuverNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">repeatLastManeuverNotification</span>()</div>
<div class="block"><p>Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#repeatLastManeuverNotification()">repeatLastManeuverNotification</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">
<h3>calculateRemainingDistanceInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">calculateRemainingDistanceInMeters</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>This method calculates the distance between the current position and given coordinates.
 The coordinates must be on the polyline.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">calculateRemainingDistanceInMeters</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the location.</p></dd>
<dt>Returns:</dt>
<dd><p>distance in meters or null if given coordinates are not on route or given
     coordinates were already traversed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>This method sets custom options that controls navigator behavior.
 Unsupported options are silently ignored.
 Undocumented options can change their meaning without going through deprecation process.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - <p>Option name</p></dd>
<dd><code>value</code> - <p>New option value</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>location</code> - <p>Current location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoute()">
<h3>getRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()</div>
<div class="block"><p>Gets the route that is being navigated.
 </p><p>Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoute()">getRoute</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoute(com.here.sdk.routing.Route)">
<h3>setRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoute</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> value)</span></div>
<div class="block"><p>Sets the route to navigate.
 </p><p>Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoute(com.here.sdk.routing.Route)">setRoute</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrackingTransportProfile()">
<h3>getTrackingTransportProfile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></span> <span class="element-name">getTrackingTransportProfile</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div class="block"><p>Gets the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrackingTransportProfile()">getTrackingTransportProfile</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">
<h3>setTrackingTransportProfile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrackingTransportProfile</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div class="block"><p>Sets the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">setTrackingTransportProfile</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrackingTransportSpecification()">
<h3>getTrackingTransportSpecification</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">getTrackingTransportSpecification</span>()</div>
<div class="block"><p>Gets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>:
 <ul>
<li><a href="sdk-for-android-navigate-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrackingTransportSpecification()">getTrackingTransportSpecification</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">
<h3>setTrackingTransportSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrackingTransportSpecification</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</span></div>
<div class="block"><p>Sets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>:
 <ul>
<li><a href="sdk-for-android-navigate-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">setTrackingTransportSpecification</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNavigableLocationListener()">
<h3>getNavigableLocationListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></span> <span class="element-name">getNavigableLocationListener</span>()</div>
<div class="block"><p>Gets the listener that notifies current location updates.
 </p><p>It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getNavigableLocationListener()">getNavigableLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">
<h3>setNavigableLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNavigableLocationListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies current location updates.
 </p><p>It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">setNavigableLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteProgressListener()">
<h3>getRouteProgressListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></span> <span class="element-name">getRouteProgressListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a route progress change occurs.
 </p><p>Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRouteProgressListener()">getRouteProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">
<h3>setRouteProgressListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a route progress change occurs.
 </p><p>Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">setRouteProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteDeviationListener()">
<h3>getRouteDeviationListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></span> <span class="element-name">getRouteDeviationListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when deviation from the route is observed.
 </p><p>Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRouteDeviationListener()">getRouteDeviationListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">
<h3>setRouteDeviationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteDeviationListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when deviation from the route is observed.
 </p><p>Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">setRouteDeviationListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventTextListener()">
<h3>getEventTextListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></span> <span class="element-name">getEventTextListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a text notification is available.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEventTextListener()">getEventTextListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventTextListener(com.here.sdk.navigation.EventTextListener)">
<h3>setEventTextListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEventTextListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a text notification is available.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEventTextListener(com.here.sdk.navigation.EventTextListener)">setEventTextListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMilestoneStatusListener()">
<h3>getMilestoneStatusListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></span> <span class="element-name">getMilestoneStatusListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 </p><p>It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()"><code>NavigatorInterface.isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getMilestoneStatusListener()">getMilestoneStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">
<h3>setMilestoneStatusListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMilestoneStatusListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 </p><p>It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()"><code>NavigatorInterface.isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">setMilestoneStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestinationReachedListener()">
<h3>getDestinationReachedListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></span> <span class="element-name">getDestinationReachedListener</span>()</div>
<div class="block"><p>Gets the listener that notify when the destination has been reached.
 </p><p>Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getDestinationReachedListener()">getDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">
<h3>setDestinationReachedListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDestinationReachedListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notify when the destination has been reached.
 </p><p>Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">setDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedWarningListener()">
<h3>getSpeedWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></span> <span class="element-name">getSpeedWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedWarningListener()">getSpeedWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">
<h3>setSpeedWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">setSpeedWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverViewLaneAssistanceListener()">
<h3>getManeuverViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></span> <span class="element-name">getManeuverViewLaneAssistanceListener</span>()</div>
<div class="block"><p>Gets the listener  to receive maneuver view lane assistance notifications.
 </p><p>Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverViewLaneAssistanceListener()">getManeuverViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">
<h3>setManeuverViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverViewLaneAssistanceListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive maneuver view lane assistance notifications.
 </p><p>Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">setManeuverViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentSituationLaneAssistanceViewListener()">
<h3>getCurrentSituationLaneAssistanceViewListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></span> <span class="element-name">getCurrentSituationLaneAssistanceViewListener</span>()</div>
<div class="block"><p>Gets the listener  to receive current situation lane assistance view notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getCurrentSituationLaneAssistanceViewListener()">getCurrentSituationLaneAssistanceViewListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">
<h3>setCurrentSituationLaneAssistanceViewListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrentSituationLaneAssistanceViewListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive current situation lane assistance view notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">setCurrentSituationLaneAssistanceViewListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnvironmentalZoneWarningListener()">
<h3>getEnvironmentalZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></span> <span class="element-name">getEnvironmentalZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive current environmental zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEnvironmentalZoneWarningListener()">getEnvironmentalZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">
<h3>setEnvironmentalZoneWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnvironmentalZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive current environmental zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">setEnvironmentalZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJunctionViewLaneAssistanceListener()">
<h3>getJunctionViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></span> <span class="element-name">getJunctionViewLaneAssistanceListener</span>()</div>
<div class="block"><p>Gets the listener  to receive junction view lane assistance notifications.
 </p><p>Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getJunctionViewLaneAssistanceListener()">getJunctionViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">
<h3>setJunctionViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setJunctionViewLaneAssistanceListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive junction view lane assistance notifications.
 </p><p>Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">setJunctionViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSafetyCameraWarningListener()">
<h3>getSafetyCameraWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></span> <span class="element-name">getSafetyCameraWarningListener</span>()</div>
<div class="block"><p>Gets the listener  to receive safety camera warning notifications.
 </p><p>If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSafetyCameraWarningListener()">getSafetyCameraWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">
<h3>setSafetyCameraWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive safety camera warning notifications.
 </p><p>If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">setSafetyCameraWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSafetyCameraWarningOptions()">
<h3>getSafetyCameraWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span class="element-name">getSafetyCameraWarningOptions</span>()</div>
<div class="block"><p>Gets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 </p><p>These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSafetyCameraWarningOptions()">getSafetyCameraWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">
<h3>setSafetyCameraWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</span></div>
<div class="block"><p>Sets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 </p><p>These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">setSafetyCameraWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDangerZoneWarningListener()">
<h3>getDangerZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></span> <span class="element-name">getDangerZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive current danger zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getDangerZoneWarningListener()">getDangerZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">
<h3>setDangerZoneWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDangerZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive current danger zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">setDangerZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictionsWarningListener()">
<h3>getTruckRestrictionsWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></span> <span class="element-name">getTruckRestrictionsWarningListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about
 truck restrictions on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTruckRestrictionsWarningListener()">getTruckRestrictionsWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">
<h3>setTruckRestrictionsWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about
 truck restrictions on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">setTruckRestrictionsWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarnerEngine()">
<h3>getWarnerEngine</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></span> <span class="element-name">getWarnerEngine</span>()</div>
<div class="block"><p>Gets the warner engine used by the navigator.
 </p><p>This engine can be used to configure navigation warnings.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getWarnerEngine()">getWarnerEngine</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Warner engine used by the navigator.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictionsWarningOptions()">
<h3>getTruckRestrictionsWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span class="element-name">getTruckRestrictionsWarningOptions</span>()</div>
<div class="block"><p>Gets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTruckRestrictionsWarningOptions()">getTruckRestrictionsWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">
<h3>setTruckRestrictionsWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</span></div>
<div class="block"><p>Sets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">setTruckRestrictionsWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostActionListener()">
<h3>getPostActionListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></span> <span class="element-name">getPostActionListener</span>()</div>
<div class="block"><p>Gets the listener  to receive post action notifications, such as a charge action at a charging station.
 </p><p>Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getPostActionListener()">getPostActionListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPostActionListener(com.here.sdk.navigation.PostActionListener)">
<h3>setPostActionListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPostActionListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive post action notifications, such as a charge action at a charging station.
 </p><p>Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setPostActionListener(com.here.sdk.navigation.PostActionListener)">setPostActionListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedLimitListener()">
<h3>getSpeedLimitListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></span> <span class="element-name">getSpeedLimitListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about the speed limit of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedLimitListener()">getSpeedLimitListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">
<h3>setSpeedLimitListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedLimitListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about the speed limit of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">setSpeedLimitListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadTextsListener()">
<h3>getRoadTextsListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></span> <span class="element-name">getRoadTextsListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about the textual attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadTextsListener()">getRoadTextsListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">
<h3>setRoadTextsListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadTextsListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about the textual attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">setRoadTextsListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadAttributesListener()">
<h3>getRoadAttributesListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></span> <span class="element-name">getRoadAttributesListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadAttributesListener()">getRoadAttributesListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">
<h3>setRoadAttributesListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadAttributesListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">setRoadAttributesListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSignWarningListener()">
<h3>getRoadSignWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></span> <span class="element-name">getRoadSignWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about road signs on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadSignWarningListener()">getRoadSignWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">
<h3>setRoadSignWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadSignWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about road signs on the current road.
 <strong>Note:</strong> This <code>RoadSignWarningListener</code> will provide
 school zone warnings only in case the speed limit inside the school zone is different than the
 default speed limit applicable for cars outside the school zone. For warnings about school zones
 regardless of their speed limits, the <code>NavigatorInterface.road_sign_warning_listener</code> should be
 used and the <code>RoadSignWarning.type</code> should be checked for value <code>RoadSignType.SCHOOL_ZONE</code>.
 The school zone warner is a zone warner, which means that for a school zone there will <em>always</em> be
 3 warnings emitted, with the <code>SchoolZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
</p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">setRoadSignWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSignWarningOptions()">
<h3>getRoadSignWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span class="element-name">getRoadSignWarningOptions</span>()</div>
<div class="block"><p>Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadSignWarningOptions()">getRoadSignWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">
<h3>setRoadSignWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoadSignWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</span></div>
<div class="block"><p>Sets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">setRoadSignWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchoolZoneWarningListener()">
<h3>getSchoolZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></span> <span class="element-name">getSchoolZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about school zones on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSchoolZoneWarningListener()">getSchoolZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">
<h3>setSchoolZoneWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about school zones on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">setSchoolZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchoolZoneWarningOptions()">
<h3>getSchoolZoneWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span class="element-name">getSchoolZoneWarningOptions</span>()</div>
<div class="block"><p>Gets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 </p><p>It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSchoolZoneWarningOptions()">getSchoolZoneWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">
<h3>setSchoolZoneWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</span></div>
<div class="block"><p>Sets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 </p><p>It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">setSchoolZoneWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealisticViewWarningListener()">
<h3>getRealisticViewWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></span> <span class="element-name">getRealisticViewWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about junction views on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRealisticViewWarningListener()">getRealisticViewWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">
<h3>setRealisticViewWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about junction views on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">setRealisticViewWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealisticViewWarningOptions()">
<h3>getRealisticViewWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span class="element-name">getRealisticViewWarningOptions</span>()</div>
<div class="block"><p>Gets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 </p><p>It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRealisticViewWarningOptions()">getRealisticViewWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">
<h3>setRealisticViewWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</span></div>
<div class="block"><p>Sets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 </p><p>It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">setRealisticViewWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBorderCrossingWarningListener()">
<h3>getBorderCrossingWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></span> <span class="element-name">getBorderCrossingWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about border crossings on the current road.
 </p><p>Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getBorderCrossingWarningListener()">getBorderCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">
<h3>setBorderCrossingWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about border crossings on the current road.
 </p><p>Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">setBorderCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBorderCrossingWarningOptions()">
<h3>getBorderCrossingWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span class="element-name">getBorderCrossingWarningOptions</span>()</div>
<div class="block"><p>Gets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 </p><p>allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getBorderCrossingWarningOptions()">getBorderCrossingWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">
<h3>setBorderCrossingWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</span></div>
<div class="block"><p>Sets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 </p><p>allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">setBorderCrossingWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTollStopWarningListener()">
<h3>getTollStopWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></span> <span class="element-name">getTollStopWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about
 the the upcoming toll stop.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTollStopWarningListener()">getTollStopWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">
<h3>setTollStopWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTollStopWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about
 the upcoming toll stop.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">setTollStopWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRailwayCrossingWarningListener()">
<h3>getRailwayCrossingWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></span> <span class="element-name">getRailwayCrossingWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about railway crossings on the current road.
 </p><p>Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRailwayCrossingWarningListener()">getRailwayCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">
<h3>setRailwayCrossingWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRailwayCrossingWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about railway crossings on the current road.
 </p><p>Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">setRailwayCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLowSpeedZoneWarningListener()">
<h3>getLowSpeedZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></span> <span class="element-name">getLowSpeedZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about low speed zones on the current road.
 </p><p>Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getLowSpeedZoneWarningListener()">getLowSpeedZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">
<h3>setLowSpeedZoneWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLowSpeedZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about low speed zones on the current road.
 </p><p>Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">setLowSpeedZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficMergeWarningListener()">
<h3>getTrafficMergeWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></span> <span class="element-name">getTrafficMergeWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about
 merging traffic to the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficMergeWarningListener()">getTrafficMergeWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">
<h3>setTrafficMergeWarningListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about
 merging traffic to the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">setTrafficMergeWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficMergeWarningOptions()">
<h3>getTrafficMergeWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span class="element-name">getTrafficMergeWarningOptions</span>()</div>
<div class="block"><p>Gets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficMergeWarningOptions()">getTrafficMergeWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">
<h3>setTrafficMergeWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</span></div>
<div class="block"><p>Sets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">setTrafficMergeWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOffRoadDestinationReachedListener()">
<h3>getOffRoadDestinationReachedListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></span> <span class="element-name">getOffRoadDestinationReachedListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when the off-road destination has been reached.
 </p><p>Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getOffRoadDestinationReachedListener()">getOffRoadDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">
<h3>setOffRoadDestinationReachedListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadDestinationReachedListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when the off-road destination has been reached.
 </p><p>Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">setOffRoadDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOffRoadProgressListener()">
<h3>getOffRoadProgressListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></span> <span class="element-name">getOffRoadProgressListener</span>()</div>
<div class="block"><p>Gets the listener that notifies about off-road progress.
 </p><p>Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getOffRoadProgressListener()">getOffRoadProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">
<h3>setOffRoadProgressListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOffRoadProgressListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies about off-road progress.
 </p><p>Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">setOffRoadProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverNotificationOptions()">
<h3>getManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></span> <span class="element-name">getManeuverNotificationOptions</span>()</div>
<div class="block"><p>Gets the maneuver notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverNotificationOptions()">getManeuverNotificationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">
<h3>setManeuverNotificationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</span></div>
<div class="block"><p>Sets the maneuver notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">setManeuverNotificationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventTextOptions()">
<h3>getEventTextOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></span> <span class="element-name">getEventTextOptions</span>()</div>
<div class="block"><p>Gets the text notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEventTextOptions()">getEventTextOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">
<h3>setEventTextOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEventTextOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</span></div>
<div class="block"><p>Sets the text notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">setEventTextOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedWarningOptions()">
<h3>getSpeedWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></span> <span class="element-name">getSpeedWarningOptions</span>()</div>
<div class="block"><p>Gets the speed warning options.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedWarningOptions()">getSpeedWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">
<h3>setSpeedWarningOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpeedWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</span></div>
<div class="block"><p>Sets the speed warning options.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">setSpeedWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableTunnelExtrapolation()">
<h3>isEnableTunnelExtrapolation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableTunnelExtrapolation</span>()</div>
<div class="block"><p>Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.
 </p><p>By default the tunnel extrapolation is enabled.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#isEnableTunnelExtrapolation()">isEnableTunnelExtrapolation</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnableTunnelExtrapolation(boolean)">
<h3>setEnableTunnelExtrapolation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableTunnelExtrapolation</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Set to <code>true</code> to enable tunnel extrapolation, set to <code>false</code> to disable tunnel extrapolation.
 </p><p>By default the tunnel extrapolation is enabled.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEnableTunnelExtrapolation(boolean)">setEnableTunnelExtrapolation</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPassthroughWaypointsHandlingEnabled()">
<h3>isPassthroughWaypointsHandlingEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPassthroughWaypointsHandlingEnabled</span>()</div>
<div class="block"><p>Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.
 </p><p>By default the handling of passthrough waypoints is disabled.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()">isPassthroughWaypointsHandlingEnabled</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPassthroughWaypointsHandlingEnabled(boolean)">
<h3>setPassthroughWaypointsHandlingEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPassthroughWaypointsHandlingEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Set to <code>true</code> enables handling of passthrough waypoints, set to <code>false</code> disables handling of passthrough waypoints.
 </p><p>By default the handling of passthrough waypoints is disabled.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setPassthroughWaypointsHandlingEnabled(boolean)">setPassthroughWaypointsHandlingEnabled</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficOnRoute()">
<h3>getTrafficOnRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></span> <span class="element-name">getTrafficOnRoute</span>()</div>
<div class="block"><p>Gets the traffic information for the current route.
 </p><p>This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficOnRoute()">getTrafficOnRoute</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">
<h3>setTrafficOnRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRoute</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</span></div>
<div class="block"><p>Sets the traffic information for the current route.
 </p><p>This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">setTrafficOnRoute</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocationManager()">
<h3>getLocationManager</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></span> <span class="element-name">getLocationManager</span>()</div>
<div class="block"><p>Gets the location manager instance used by the navigator.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getLocationManager()">getLocationManager</a></code> in interface <code><a href="sdk-for-android-navigate-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>The location manager used by the navigator for map-matched location processing.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
