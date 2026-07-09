---
title: "Navigator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-navigator"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Navigator.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.Navigator</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Navigator</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></span></div>
<div className="block"><p>This class provides the basic navigation functionality. It provides
 notifications about current map-matched location updates (see <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation"><code>NavigableLocation</code></a>).
 And, if a route has been set, about the route progress (see <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress" title="class in com.here.sdk.navigation"><code>RouteProgress</code></a>),
 route deviations (see <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation" title="class in com.here.sdk.navigation"><code>RouteDeviation</code></a>) and maneuver notifications (see
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a>).
 All transport modes are supported for turn-by-turn navigation, except for public transit.
 Public transit routes may lead to unsafe and unexpected results.
 Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and
 turn-by-turn bus instructions may not be as appropriate as expected.
 The <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport"><code>TransportMode</code></a> is determined from the provided <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> instance,
 but the actual <a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing"><code>SectionTransportMode</code></a> can vary along a route, for example, when a
 ferry must be taken. When no route is set, the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation"><code>NavigableLocation</code></a> assumes a drive
 scenario.
 This class continuously reacts to new locations provided from a location source and acts as a
 <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a>.
 The accuracy of the positioning increases with the update frequency. At least one update per second
 should be provided. More information can be found at <code>LocationAccuracy.NAVIGATION</code>.
 <strong>Note:</strong>
 Even without provided locations, for example, while driving through a tunnel, this class
 can interpolate missing location events and still send <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation"><code>NavigableLocation</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress" title="class in com.here.sdk.navigation"><code>RouteProgress</code></a> and maneuver notifications.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-navigator#%3Cinit%3E()">Navigator</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-navigator#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">Navigator</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>Navigator</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Navigator</span>()
          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>Navigator</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Navigator</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getAvailableLanguagesForManeuverNotifications()">
<h3>getAvailableLanguagesForManeuverNotifications</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a>&gt;</span> <span className="element-name">getAvailableLanguagesForManeuverNotifications</span>()</div>
<div className="block"><p>Returns the list of languages for maneuver notification currently available in the SDK.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>the list of languages for maneuver notification currently available in the SDK.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuver(int)">
<h3>getManeuver</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span className="element-name">getManeuver</span><wbr/><span className="parameters">(int index)</span></div>
<div className="block"><p>Returns maneuver at the given index.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuver(int)">getManeuver</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - <p>The index of maneuver requested.</p></dd>
<dt>Returns:</dt>
<dd><p>The maneuver if it exists or otherwise <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">
<h3>getManeuverNotificationTimingOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></span> <span className="element-name">getManeuverNotificationTimingOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</span></div>
<div className="block"><p>Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
 The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes
 of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function
 for the same combination of transport mode and timing profile.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">getManeuverNotificationTimingOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dt>Returns:</dt>
<dd><p>The timing options with default values.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">
<h3>setManeuverNotificationTimingOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setManeuverNotificationTimingOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</span></div>
<div className="block"><p>Set timing option values for the combination of transport mode and timing profile.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">setManeuverNotificationTimingOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dd><code>options</code> - <p>The timing options.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when options has invalid value, see <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation"><code>ManeuverNotificationTimingOptions</code></a> for
     more details about options.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">
<h3>getWarningNotificationDistances</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span className="element-name">getWarningNotificationDistances</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span></div>
<div className="block"><p>Returns the warning notification distances for the requested warning type. The return value can be used as the
 base for configuring warning notification distances. Configure the relevant attributes of this object according
 to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
 warning type and the modified warning notification distances object.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">getWarningNotificationDistances</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the notification distances will be returned.</p></dd>
<dt>Returns:</dt>
<dd><p>The notification distances for the given warning type.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setWarningNotificationDistances</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setWarningNotificationDistances</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div className="block"><p>Set the warning notification distances for the specified warning types.
 <strong>Note:</strong> The warning notification distances are set for most warners.
 This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
 Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code>TimingProfile</code>.
 If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
 Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code>TimingProfile</code>.
 Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
 seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">setWarningNotificationDistances</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the warning notification distances will be set.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be set for the specified warning types.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when the warning_type is [WarningType.SCHOOL_ZONE] or the options have invalid values,
     see <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> for more details about warning notification distances.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="repeatLastManeuverNotification()">
<h3>repeatLastManeuverNotification</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">repeatLastManeuverNotification</span>()</div>
<div className="block"><p>Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#repeatLastManeuverNotification()">repeatLastManeuverNotification</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">
<h3>calculateRemainingDistanceInMeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">calculateRemainingDistanceInMeters</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>This method calculates the distance between the current position and given coordinates.
 The coordinates must be on the polyline.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">calculateRemainingDistanceInMeters</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the location.</p></dd>
<dt>Returns:</dt>
<dd><p>distance in meters or null if given coordinates are not on route or given
     coordinates were already traversed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCustomOption</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>This method sets custom options that controls navigator behavior.
 Unsupported options are silently ignored.
 Undocumented options can change their meaning without going through deprecation process.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - <p>Option name</p></dd>
<dd><code>value</code> - <p>New option value</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onLocationUpdated(com.here.sdk.core.Location)">
<h3>onLocationUpdated</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onLocationUpdated</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>Called each time a new location is available.
 In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
 it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
 object so that the HERE SDK can map-match the locations properly.
 If the <code>Location.time</code> parameter is missing, the location will be ignored.
 For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
 parameters for each <code>Location</code> object.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>location</code> - <p>Current location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoute()">
<h3>getRoute</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span className="element-name">getRoute</span>()</div>
<div className="block"><p>Gets the route that is being navigated.
 Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoute()">getRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoute(com.here.sdk.routing.Route)">
<h3>setRoute</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoute</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span></div>
<div className="block"><p>Sets the route to navigate.
 Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoute(com.here.sdk.routing.Route)">setRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrackingTransportProfile()">
<h3>getTrackingTransportProfile</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></span> <span className="element-name">getTrackingTransportProfile</span>()</div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div className="block"><p>Gets the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 Currently used members of <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrackingTransportProfile()">getTrackingTransportProfile</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">
<h3>setTrackingTransportProfile</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrackingTransportProfile</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div className="block"><p>Sets the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 Currently used members of <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">setTrackingTransportProfile</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrackingTransportSpecification()">
<h3>getTrackingTransportSpecification</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span className="element-name">getTrackingTransportSpecification</span>()</div>
<div className="block"><p>Gets the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 Currently used members of <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
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
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrackingTransportSpecification()">getTrackingTransportSpecification</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">
<h3>setTrackingTransportSpecification</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrackingTransportSpecification</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</span></div>
<div className="block"><p>Sets the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 Currently used members of <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
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
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">setTrackingTransportSpecification</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNavigableLocationListener()">
<h3>getNavigableLocationListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></span> <span className="element-name">getNavigableLocationListener</span>()</div>
<div className="block"><p>Gets the listener that notifies current location updates.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getNavigableLocationListener()">getNavigableLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">
<h3>setNavigableLocationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setNavigableLocationListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies current location updates.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">setNavigableLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRouteProgressListener()">
<h3>getRouteProgressListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></span> <span className="element-name">getRouteProgressListener</span>()</div>
<div className="block"><p>Gets the listener that notifies when a route progress change occurs.
 Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRouteProgressListener()">getRouteProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">
<h3>setRouteProgressListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRouteProgressListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies when a route progress change occurs.
 Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">setRouteProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRouteDeviationListener()">
<h3>getRouteDeviationListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></span> <span className="element-name">getRouteDeviationListener</span>()</div>
<div className="block"><p>Gets the listener that notifies when deviation from the route is observed.
 Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRouteDeviationListener()">getRouteDeviationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">
<h3>setRouteDeviationListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRouteDeviationListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies when deviation from the route is observed.
 Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">setRouteDeviationListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEventTextListener()">
<h3>getEventTextListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></span> <span className="element-name">getEventTextListener</span>()</div>
<div className="block"><p>Gets the listener that notifies when a text notification is available.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEventTextListener()">getEventTextListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setEventTextListener(com.here.sdk.navigation.EventTextListener)">
<h3>setEventTextListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setEventTextListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies when a text notification is available.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEventTextListener(com.here.sdk.navigation.EventTextListener)">setEventTextListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMilestoneStatusListener()">
<h3>getMilestoneStatusListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></span> <span className="element-name">getMilestoneStatusListener</span>()</div>
<div className="block"><p>Gets the listener that notifies when a <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()"><code>NavigatorInterface.isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getMilestoneStatusListener()">getMilestoneStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">
<h3>setMilestoneStatusListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMilestoneStatusListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies when a <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()"><code>NavigatorInterface.isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">setMilestoneStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDestinationReachedListener()">
<h3>getDestinationReachedListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></span> <span className="element-name">getDestinationReachedListener</span>()</div>
<div className="block"><p>Gets the listener that notify when the destination has been reached.
 Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getDestinationReachedListener()">getDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">
<h3>setDestinationReachedListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDestinationReachedListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notify when the destination has been reached.
 Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">setDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedWarningListener()">
<h3>getSpeedWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></span> <span className="element-name">getSpeedWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedWarningListener()">getSpeedWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">
<h3>setSpeedWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSpeedWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">setSpeedWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuverViewLaneAssistanceListener()">
<h3>getManeuverViewLaneAssistanceListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></span> <span className="element-name">getManeuverViewLaneAssistanceListener</span>()</div>
<div className="block"><p>Gets the listener  to receive maneuver view lane assistance notifications.
 Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverViewLaneAssistanceListener()">getManeuverViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">
<h3>setManeuverViewLaneAssistanceListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setManeuverViewLaneAssistanceListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive maneuver view lane assistance notifications.
 Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">setManeuverViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCurrentSituationLaneAssistanceViewListener()">
<h3>getCurrentSituationLaneAssistanceViewListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></span> <span className="element-name">getCurrentSituationLaneAssistanceViewListener</span>()</div>
<div className="block"><p>Gets the listener  to receive current situation lane assistance view notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getCurrentSituationLaneAssistanceViewListener()">getCurrentSituationLaneAssistanceViewListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">
<h3>setCurrentSituationLaneAssistanceViewListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCurrentSituationLaneAssistanceViewListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive current situation lane assistance view notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">setCurrentSituationLaneAssistanceViewListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEnvironmentalZoneWarningListener()">
<h3>getEnvironmentalZoneWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></span> <span className="element-name">getEnvironmentalZoneWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive current environmental zones notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEnvironmentalZoneWarningListener()">getEnvironmentalZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">
<h3>setEnvironmentalZoneWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setEnvironmentalZoneWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive current environmental zones notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">setEnvironmentalZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getJunctionViewLaneAssistanceListener()">
<h3>getJunctionViewLaneAssistanceListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></span> <span className="element-name">getJunctionViewLaneAssistanceListener</span>()</div>
<div className="block"><p>Gets the listener  to receive junction view lane assistance notifications.
 Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getJunctionViewLaneAssistanceListener()">getJunctionViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">
<h3>setJunctionViewLaneAssistanceListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setJunctionViewLaneAssistanceListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive junction view lane assistance notifications.
 Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">setJunctionViewLaneAssistanceListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSafetyCameraWarningListener()">
<h3>getSafetyCameraWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></span> <span className="element-name">getSafetyCameraWarningListener</span>()</div>
<div className="block"><p>Gets the listener  to receive safety camera warning notifications.
 If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSafetyCameraWarningListener()">getSafetyCameraWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">
<h3>setSafetyCameraWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSafetyCameraWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive safety camera warning notifications.
 If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">setSafetyCameraWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSafetyCameraWarningOptions()">
<h3>getSafetyCameraWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span className="element-name">getSafetyCameraWarningOptions</span>()</div>
<div className="block"><p>Gets safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSafetyCameraWarningOptions()">getSafetyCameraWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">
<h3>setSafetyCameraWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSafetyCameraWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</span></div>
<div className="block"><p>Sets safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">setSafetyCameraWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDangerZoneWarningListener()">
<h3>getDangerZoneWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></span> <span className="element-name">getDangerZoneWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive current danger zones notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getDangerZoneWarningListener()">getDangerZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">
<h3>setDangerZoneWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDangerZoneWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive current danger zones notifications.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">setDangerZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTruckRestrictionsWarningListener()">
<h3>getTruckRestrictionsWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></span> <span className="element-name">getTruckRestrictionsWarningListener</span>()</div>
<div className="block"><p>Gets the listener  to receive notifications about
 truck restrictions on the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTruckRestrictionsWarningListener()">getTruckRestrictionsWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">
<h3>setTruckRestrictionsWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTruckRestrictionsWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive notifications about
 truck restrictions on the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">setTruckRestrictionsWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWarnerEngine()">
<h3>getWarnerEngine</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></span> <span className="element-name">getWarnerEngine</span>()</div>
<div className="block"><p>Gets the warner engine used by the navigator.
 This engine can be used to configure navigation warnings.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getWarnerEngine()">getWarnerEngine</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Warner engine used by the navigator.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTruckRestrictionsWarningOptions()">
<h3>getTruckRestrictionsWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span className="element-name">getTruckRestrictionsWarningOptions</span>()</div>
<div className="block"><p>Gets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTruckRestrictionsWarningOptions()">getTruckRestrictionsWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">
<h3>setTruckRestrictionsWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTruckRestrictionsWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</span></div>
<div className="block"><p>Sets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">setTruckRestrictionsWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPostActionListener()">
<h3>getPostActionListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></span> <span className="element-name">getPostActionListener</span>()</div>
<div className="block"><p>Gets the listener  to receive post action notifications, such as a charge action at a charging station.
 Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getPostActionListener()">getPostActionListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPostActionListener(com.here.sdk.navigation.PostActionListener)">
<h3>setPostActionListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPostActionListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive post action notifications, such as a charge action at a charging station.
 Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setPostActionListener(com.here.sdk.navigation.PostActionListener)">setPostActionListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedLimitListener()">
<h3>getSpeedLimitListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></span> <span className="element-name">getSpeedLimitListener</span>()</div>
<div className="block"><p>Gets the listener  to receive notifications about the speed limit of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedLimitListener()">getSpeedLimitListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">
<h3>setSpeedLimitListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSpeedLimitListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive notifications about the speed limit of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">setSpeedLimitListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadTextsListener()">
<h3>getRoadTextsListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></span> <span className="element-name">getRoadTextsListener</span>()</div>
<div className="block"><p>Gets the listener  to receive notifications about the textual attributes of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadTextsListener()">getRoadTextsListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">
<h3>setRoadTextsListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoadTextsListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive notifications about the textual attributes of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">setRoadTextsListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadAttributesListener()">
<h3>getRoadAttributesListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></span> <span className="element-name">getRoadAttributesListener</span>()</div>
<div className="block"><p>Gets the listener  to receive notifications about attributes of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadAttributesListener()">getRoadAttributesListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">
<h3>setRoadAttributesListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoadAttributesListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</span></div>
<div className="block"><p>Sets the listener  to receive notifications about attributes of the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">setRoadAttributesListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadSignWarningListener()">
<h3>getRoadSignWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></span> <span className="element-name">getRoadSignWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about road signs on the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadSignWarningListener()">getRoadSignWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">
<h3>setRoadSignWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoadSignWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about road signs on the current road.
 <strong>Note:</strong> This <code>RoadSignWarningListener</code> will provide
 school zone warnings only in case the speed limit inside the school zone is different than the
 default speed limit applicable for cars outside the school zone. For warnings about school zones
 regardless of their speed limits, the <code>NavigatorInterface.road_sign_warning_listener</code> should be
 used and the <code>RoadSignWarning.type</code> should be checked for value <code>RoadSignType.SCHOOL_ZONE</code>.
 The school zone warner is a zone warner, which means that for a school zone there will <em>always</em> be
 3 warnings emitted, with the <code>SchoolZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">setRoadSignWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadSignWarningOptions()">
<h3>getRoadSignWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span className="element-name">getRoadSignWarningOptions</span>()</div>
<div className="block"><p>Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRoadSignWarningOptions()">getRoadSignWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">
<h3>setRoadSignWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoadSignWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</span></div>
<div className="block"><p>Sets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">setRoadSignWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSchoolZoneWarningListener()">
<h3>getSchoolZoneWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></span> <span className="element-name">getSchoolZoneWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about school zones on the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSchoolZoneWarningListener()">getSchoolZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">
<h3>setSchoolZoneWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSchoolZoneWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about school zones on the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">setSchoolZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSchoolZoneWarningOptions()">
<h3>getSchoolZoneWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span className="element-name">getSchoolZoneWarningOptions</span>()</div>
<div className="block"><p>Gets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSchoolZoneWarningOptions()">getSchoolZoneWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">
<h3>setSchoolZoneWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSchoolZoneWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</span></div>
<div className="block"><p>Sets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">setSchoolZoneWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRealisticViewWarningListener()">
<h3>getRealisticViewWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></span> <span className="element-name">getRealisticViewWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about junction views on the current road.
 Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRealisticViewWarningListener()">getRealisticViewWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">
<h3>setRealisticViewWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRealisticViewWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about junction views on the current road.
 Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">setRealisticViewWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRealisticViewWarningOptions()">
<h3>getRealisticViewWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span className="element-name">getRealisticViewWarningOptions</span>()</div>
<div className="block"><p>Gets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRealisticViewWarningOptions()">getRealisticViewWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">
<h3>setRealisticViewWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRealisticViewWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</span></div>
<div className="block"><p>Sets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">setRealisticViewWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBorderCrossingWarningListener()">
<h3>getBorderCrossingWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></span> <span className="element-name">getBorderCrossingWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about border crossings on the current road.
 Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getBorderCrossingWarningListener()">getBorderCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">
<h3>setBorderCrossingWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBorderCrossingWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about border crossings on the current road.
 Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">setBorderCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBorderCrossingWarningOptions()">
<h3>getBorderCrossingWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span className="element-name">getBorderCrossingWarningOptions</span>()</div>
<div className="block"><p>Gets border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getBorderCrossingWarningOptions()">getBorderCrossingWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">
<h3>setBorderCrossingWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBorderCrossingWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</span></div>
<div className="block"><p>Sets border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">setBorderCrossingWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTollStopWarningListener()">
<h3>getTollStopWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></span> <span className="element-name">getTollStopWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about
 the the upcoming toll stop.
 Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTollStopWarningListener()">getTollStopWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">
<h3>setTollStopWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTollStopWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about
 the upcoming toll stop.
 Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">setTollStopWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRailwayCrossingWarningListener()">
<h3>getRailwayCrossingWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></span> <span className="element-name">getRailwayCrossingWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about railway crossings on the current road.
 Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getRailwayCrossingWarningListener()">getRailwayCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">
<h3>setRailwayCrossingWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRailwayCrossingWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about railway crossings on the current road.
 Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">setRailwayCrossingWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLowSpeedZoneWarningListener()">
<h3>getLowSpeedZoneWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></span> <span className="element-name">getLowSpeedZoneWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about low speed zones on the current road.
 Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getLowSpeedZoneWarningListener()">getLowSpeedZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">
<h3>setLowSpeedZoneWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setLowSpeedZoneWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about low speed zones on the current road.
 Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">setLowSpeedZoneWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficMergeWarningListener()">
<h3>getTrafficMergeWarningListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></span> <span className="element-name">getTrafficMergeWarningListener</span>()</div>
<div className="block"><p>Gets the listener to receive notifications about
 merging traffic to the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficMergeWarningListener()">getTrafficMergeWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">
<h3>setTrafficMergeWarningListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrafficMergeWarningListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</span></div>
<div className="block"><p>Sets the listener to receive notifications about
 merging traffic to the current road.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">setTrafficMergeWarningListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficMergeWarningOptions()">
<h3>getTrafficMergeWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span className="element-name">getTrafficMergeWarningOptions</span>()</div>
<div className="block"><p>Gets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficMergeWarningOptions()">getTrafficMergeWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">
<h3>setTrafficMergeWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrafficMergeWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</span></div>
<div className="block"><p>Sets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">setTrafficMergeWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOffRoadDestinationReachedListener()">
<h3>getOffRoadDestinationReachedListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></span> <span className="element-name">getOffRoadDestinationReachedListener</span>()</div>
<div className="block"><p>Gets the listener that notifies when the off-road destination has been reached.
 Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getOffRoadDestinationReachedListener()">getOffRoadDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">
<h3>setOffRoadDestinationReachedListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOffRoadDestinationReachedListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies when the off-road destination has been reached.
 Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">setOffRoadDestinationReachedListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOffRoadProgressListener()">
<h3>getOffRoadProgressListener</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></span> <span className="element-name">getOffRoadProgressListener</span>()</div>
<div className="block"><p>Gets the listener that notifies about off-road progress.
 Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getOffRoadProgressListener()">getOffRoadProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">
<h3>setOffRoadProgressListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOffRoadProgressListener</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</span></div>
<div className="block"><p>Sets the listener that notifies about off-road progress.
 Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">setOffRoadProgressListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuverNotificationOptions()">
<h3>getManeuverNotificationOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></span> <span className="element-name">getManeuverNotificationOptions</span>()</div>
<div className="block"><p>Gets the maneuver notification options.
 Notifications are only available if a route is present.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getManeuverNotificationOptions()">getManeuverNotificationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">
<h3>setManeuverNotificationOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setManeuverNotificationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</span></div>
<div className="block"><p>Sets the maneuver notification options.
 Notifications are only available if a route is present.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">setManeuverNotificationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEventTextOptions()">
<h3>getEventTextOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></span> <span className="element-name">getEventTextOptions</span>()</div>
<div className="block"><p>Gets the text notification options.
 Notifications are only available if a route is present.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getEventTextOptions()">getEventTextOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">
<h3>setEventTextOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setEventTextOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</span></div>
<div className="block"><p>Sets the text notification options.
 Notifications are only available if a route is present.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">setEventTextOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedWarningOptions()">
<h3>getSpeedWarningOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></span> <span className="element-name">getSpeedWarningOptions</span>()</div>
<div className="block"><p>Gets the speed warning options.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getSpeedWarningOptions()">getSpeedWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">
<h3>setSpeedWarningOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSpeedWarningOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</span></div>
<div className="block"><p>Sets the speed warning options.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">setSpeedWarningOptions</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isEnableTunnelExtrapolation()">
<h3>isEnableTunnelExtrapolation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isEnableTunnelExtrapolation</span>()</div>
<div className="block"><p>Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.
 By default the tunnel extrapolation is enabled.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#isEnableTunnelExtrapolation()">isEnableTunnelExtrapolation</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setEnableTunnelExtrapolation(boolean)">
<h3>setEnableTunnelExtrapolation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setEnableTunnelExtrapolation</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Set to <code>true</code> to enable tunnel extrapolation, set to <code>false</code> to disable tunnel extrapolation.
 By default the tunnel extrapolation is enabled.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setEnableTunnelExtrapolation(boolean)">setEnableTunnelExtrapolation</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isPassthroughWaypointsHandlingEnabled()">
<h3>isPassthroughWaypointsHandlingEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isPassthroughWaypointsHandlingEnabled</span>()</div>
<div className="block"><p>Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.
 By default the handling of passthrough waypoints is disabled.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#isPassthroughWaypointsHandlingEnabled()">isPassthroughWaypointsHandlingEnabled</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPassthroughWaypointsHandlingEnabled(boolean)">
<h3>setPassthroughWaypointsHandlingEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPassthroughWaypointsHandlingEnabled</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Set to <code>true</code> enables handling of passthrough waypoints, set to <code>false</code> disables handling of passthrough waypoints.
 By default the handling of passthrough waypoints is disabled.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setPassthroughWaypointsHandlingEnabled(boolean)">setPassthroughWaypointsHandlingEnabled</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficOnRoute()">
<h3>getTrafficOnRoute</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></span> <span className="element-name">getTrafficOnRoute</span>()</div>
<div className="block"><p>Gets the traffic information for the current route.
 This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getTrafficOnRoute()">getTrafficOnRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Returns:</dt>
<dd><p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">
<h3>setTrafficOnRoute</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrafficOnRoute</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</span></div>
<div className="block"><p>Sets the traffic information for the current route.
 This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">setTrafficOnRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLocationManager()">
<h3>getLocationManager</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></span> <span className="element-name">getLocationManager</span>()</div>
<div className="block"><p>Gets the location manager instance used by the navigator.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-navigatorinterface#getLocationManager()">getLocationManager</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a></code></dd>
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
</div>



</div>
`
}</HTMLBlock>
