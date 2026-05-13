---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-navigator"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Navigator.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Navigator"></a>
<a title="Navigator Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Navigator Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Navigator</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Navigator</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Navigator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Navigator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides the basic navigation functionality. It provides
notifications about current map-matched location updates (see <code><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></code>).
And, if a route has been set, about the route progress (see <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeprogress">RouteProgress</a></code>),
route deviations (see <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routedeviation">RouteDeviation</a></code>) and maneuver notifications (see
<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-eventtextdelegate">EventTextDelegate</a></code>).</p>
<p>All transport modes are supported for turn-by-turn navigation, except for public transit.
Public transit routes may lead to unsafe and unexpected results.</p>
<p>Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and
turn-by-turn bus instructions may not be as appropriate as expected.</p>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-enums-transportmode">TransportMode</a></code> is determined from the provided <code><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></code> instance,
but the actual <code><a href="sdk-for-ios-navigate-api-reference-..-enums-sectiontransportmode">SectionTransportMode</a></code> can vary along a route, for example, when a
ferry must be taken. When no route is set, the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></code> assumes a drive
scenario.</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-locationdelegate">LocationDelegate</a></code>.
The accuracy of the positioning increases with the update frequency. At least one update per second
should be provided. More information can be found at <code>LocationAccuracy.NAVIGATION</code>.</p>
<p><strong>Note:</strong>
Even without provided locations, for example, while driving through a tunnel, this class
can interpolate missing location events and still send <code><a href="sdk-for-ios-navigate-api-reference-..-structs-navigablelocation">NavigableLocation</a></code>,
<code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeprogress">RouteProgress</a></code> and maneuver notifications.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk9NavigatorCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC9sdkEngineAcA09SDKNativeD0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC9sdkEngineAcA09SDKNativeD0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>A SDKEngine instance.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC5routeAA5RouteCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/route"></a>
<a class="token" href="#/s:7heresdk9NavigatorC5routeAA5RouteCSgvp">route</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route to navigate.
Gets and sets the route that is being navigated.
If not set, only the current location information will be
provided through <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigablelocationdelegate">NavigableLocationDelegate</a></code>.
If set, both route progress (<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-routeprogressdelegate">RouteProgressDelegate</a></code>) and route deviation
(<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-routedeviationdelegate">RouteDeviationDelegate</a></code>) will receive notifications on updates.
A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC24trackingTransportProfileAA0dE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportProfile"></a>
<a class="token" href="#/s:7heresdk9NavigatorC24trackingTransportProfileAA0dE0VSgvp">trackingTransportProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportprofile">TransportProfile</a></code> can be defined with a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-vehicleprofile">VehicleProfile</a></code>.
A vehicle profile can have several parameters such as <code><a href="sdk-for-ios-navigate-api-reference-..-enums-vehicletype">VehicleType</a></code> to set the
source of information describing the vehicle.
The default is a <code><a href="../Enums/VehicleType.html#/s:7heresdk11VehicleTypeO3caryA2CmF">VehicleType.car</a></code> profile.</p>
<p>Currently used members of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportprofile">TransportProfile</a></code></p>
<ul>
<li><code><a href="sdk-for-ios-navigate-api-reference-..-enums-vehicletype">VehicleType</a></code>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:

<ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">trackingTransportProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-transportprofile">TransportProfile</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC30trackingTransportSpecificationAA0dE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportSpecification"></a>
<a class="token" href="#/s:7heresdk9NavigatorC30trackingTransportSpecificationAA0dE0VSgvp">trackingTransportSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the transport specification for the <code>Navigator</code>, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportspecification">TransportSpecification</a></code> must have the <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> set.
A transport specification can have several parameters defined such as <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">VehicleSpecification.lengthInCentimeters</a></code>
defined in <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> to set the source of information describing the vehicle.
By default the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportspecification">TransportSpecification</a></code> will have the transport mode set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</p>
<p>Currently used members of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportspecification">TransportSpecification</a></code></p>
<ul>
<li><code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code>: Sets the transport mode.</li>
<li>From <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code>:

<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>: Required for truck related speed information.</li>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code>: Required for truck related speed information.</li>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code>: Additional truck definition for more specific truck speed information.</li>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">VehicleSpecification.lengthInCentimeters</a></code>: Additional truck definition for more specific truck speed information.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trackingTransportSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-transportspecification">TransportSpecification</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC25navigableLocationDelegateAA09NavigabledE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/navigableLocationDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC25navigableLocationDelegateAA09NavigabledE0_pSgvp">navigableLocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the current location.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">navigableLocationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigablelocationdelegate">NavigableLocationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC21routeProgressDelegateAA05RoutedE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeProgressDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC21routeProgressDelegateAA05RoutedE0_pSgvp">routeProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about navigation route progress.
Route progress notifications only occurs if the route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">routeProgressDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-routeprogressdelegate">RouteProgressDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC22routeDeviationDelegateAA05RoutedE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeDeviationDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC22routeDeviationDelegateAA05RoutedE0_pSgvp">routeDeviationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about deviations from the route if any occurs.
Route deviation notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">routeDeviationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-routedeviationdelegate">RouteDeviationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC17eventTextDelegateAA05EventdE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC17eventTextDelegateAA05EventdE0_pSgvp">eventTextDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive text notifications when they are available.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">eventTextDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-eventtextdelegate">EventTextDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC23milestoneStatusDelegateAA09MilestonedE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/milestoneStatusDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC23milestoneStatusDelegateAA09MilestonedE0_pSgvp">milestoneStatusDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the arrival at each <code><a href="sdk-for-ios-navigate-api-reference-..-structs-milestone">Milestone</a></code> or missing it.
It informs on all waypoints (passed or missed) that
are of type <code><a href="../Enums/MilestoneType.html#/s:7heresdk13MilestoneTypeO8stopoveryA2CmF">MilestoneType.stopover</a></code> but excludes the
starting waypoint.
Waypoints of type <code><a href="../Enums/MilestoneType.html#/s:7heresdk13MilestoneTypeO11passthroughyA2CmF">MilestoneType.passthrough</a></code> are excluded, by default,
but can be included via <code><a href="../Classes/Navigator.html#/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">isPassthroughWaypointsHandlingEnabled</a></code>.
Milestone status notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">milestoneStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC26destinationReachedDelegateAA011DestinationdE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/destinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC26destinationReachedDelegateAA011DestinationdE0_pSgvp">destinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the arrival at the destination.
Destination reached notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">destinationReachedDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-destinationreacheddelegate">DestinationReachedDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC20speedWarningDelegateAA05SpeeddE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC20speedWarningDelegateAA05SpeeddE0_pSgvp">speedWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">speedWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-speedwarningdelegate">SpeedWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverdefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverdefG0_pSgvp">maneuverViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive maneuver view lane assistance notifications.
Maneuver view lane assistance notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">maneuverViewLaneAssistanceDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentdefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentSituationLaneAssistanceViewDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentdefgH0_pSgvp">currentSituationLaneAssistanceViewDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive current situation lane assistance view notifications.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">currentSituationLaneAssistanceViewDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentaldeG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/environmentalZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentaldeG0_pSgvp">environmentalZoneWarningListenerDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notification on approaching environmental zones.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">environmentalZoneWarningListenerDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC34junctionViewLaneAssistanceDelegateAA08JunctiondefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC34junctionViewLaneAssistanceDelegateAA08JunctiondefG0_pSgvp">junctionViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive junction view lane assistance notifications.
Junction view lane assistance notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">junctionViewLaneAssistanceDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27safetyCameraWarningDelegateAA06SafetydeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27safetyCameraWarningDelegateAA06SafetydeF0_pSgvp">safetyCameraWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive safety camera warner notifications.
If a delegate delegate is present, notifications about
safety speed cameras will be also sent via <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a></code>.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">safetyCameraWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC26safetyCameraWarningOptionsAA06SafetydeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC26safetyCameraWarningOptionsAA06SafetydeF0Vvp">safetyCameraWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera warning options to be passed to <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a></code>.
These options allow the enabling or disabling the text notification for the warner.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">safetyCameraWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC33dangerZoneWarningListenerDelegateAA06DangerdeG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dangerZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC33dangerZoneWarningListenerDelegateAA06DangerdeG0_pSgvp">dangerZoneWarningListenerDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notification on approaching danger zones.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">dangerZoneWarningListenerDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC32truckRestrictionsWarningDelegateAA05TruckdeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC32truckRestrictionsWarningDelegateAA05TruckdeF0_pSgvp">truckRestrictionsWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about truck restrictions on the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">truckRestrictionsWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC12warnerEngineAA06WarnerD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warnerEngine"></a>
<a class="token" href="#/s:7heresdk9NavigatorC12warnerEngineAA06WarnerD0Cvp">warnerEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Warner engine used by the navigator.
This engine can be used to configure navigation warnings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">warnerEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-warnerengine">WarnerEngine</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC31truckRestrictionsWarningOptionsAA05TruckdeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC31truckRestrictionsWarningOptionsAA05TruckdeF0Vvp">truckRestrictionsWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckRestrictionsWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC18postActionDelegateAA04PostdE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postActionDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC18postActionDelegateAA04PostdE0_pSgvp">postActionDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive post action notifications, such as a charge action at a charging station.
Post actions notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">postActionDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-postactiondelegate">PostActionDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC18speedLimitDelegateAA05SpeeddE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC18speedLimitDelegateAA05SpeeddE0_pSgvp">speedLimitDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the speed limit of the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">speedLimitDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-speedlimitdelegate">SpeedLimitDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC17roadTextsDelegateAA04RoaddE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadTextsDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC17roadTextsDelegateAA04RoaddE0_pSgvp">roadTextsDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the textual attributes of the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">roadTextsDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-roadtextsdelegate">RoadTextsDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC22roadAttributesDelegateAA04RoaddE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadAttributesDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC22roadAttributesDelegateAA04RoaddE0_pSgvp">roadAttributesDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about attributes of the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">roadAttributesDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-roadattributesdelegate">RoadAttributesDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC23roadSignWarningDelegateAA04RoaddeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC23roadSignWarningDelegateAA04RoaddeF0_pSgvp">roadSignWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about road signs on the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">roadSignWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC22roadSignWarningOptionsAA04RoaddeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC22roadSignWarningOptionsAA04RoaddeF0Vvp">roadSignWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road sign warning options that allow to filter road sings to be passed to <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadSignWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-roadsignwarningoptions">RoadSignWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC25schoolZoneWarningDelegateAA06SchooldeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC25schoolZoneWarningDelegateAA06SchooldeF0_pSgvp">schoolZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about school zones on the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
school zones on the current road.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">schoolZoneWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC24schoolZoneWarningOptionsAA06SchooldeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC24schoolZoneWarningOptionsAA06SchooldeF0Vvp">schoolZoneWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>School zone warning options
It allow to configure school zone notifications to be passed to
<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">schoolZoneWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC28realisticViewWarningDelegateAA09RealisticdeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC28realisticViewWarningDelegateAA09RealisticdeF0_pSgvp">realisticViewWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about junction views on the current road.
Setting <code>nil</code> value to the delegate will unset
the delegate.
This feature requires a map version greater or equal to 67 in order to function properly.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">realisticViewWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27realisticViewWarningOptionsAA09RealisticdeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27realisticViewWarningOptionsAA09RealisticdeF0Vvp">realisticViewWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Realistic view warning options.
It allow to filter realistic views to be passed to <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a></code>.</p>
<ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">realisticViewWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC29borderCrossingWarningDelegateAA06BorderdeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC29borderCrossingWarningDelegateAA06BorderdeF0_pSgvp">borderCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about border crossings on the current road.
Border crossing notifications are given only if a route is present.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">borderCrossingWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC28borderCrossingWarningOptionsAA06BorderdeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC28borderCrossingWarningOptionsAA06BorderdeF0Vvp">borderCrossingWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Border crossing warning options to be passed to <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a></code>. These options
allow the filtering of the border crossing warnings received and set the notification distances.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">borderCrossingWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC23tollStopWarningDelegateAA04TolldeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollStopWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC23tollStopWarningDelegateAA04TolldeF0_pSgvp">tollStopWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive information on the upcoming toll stop.
Setting <code>nil</code> value to the delegate will unset
the delegate.
This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">tollStopWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC30railwayCrossingWarningDelegateAA07RailwaydeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC30railwayCrossingWarningDelegateAA07RailwaydeF0_pSgvp">railwayCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about railway crossings on the current road.
Railway crossing notifications are given regardless if a route is set.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">railwayCrossingWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27lowSpeedZoneWarningDelegateAA03LowdefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lowSpeedZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27lowSpeedZoneWarningDelegateAA03LowdefG0_pSgvp">lowSpeedZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about low speed zones on the current road.
Low speed zone notifications are given regardless if a route is set. This delegate is currently
available <em>only</em> for Japan.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">lowSpeedZoneWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27trafficMergeWarningDelegateAA07TrafficdeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27trafficMergeWarningDelegateAA07TrafficdeF0_pSgvp">trafficMergeWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about merging traffic to the current road.
Setting <code>nil</code> value to the delegate will unset the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">trafficMergeWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC26trafficMergeWarningOptionsAA07TrafficdeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC26trafficMergeWarningOptionsAA07TrafficdeF0Vvp">trafficMergeWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficMergeWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC33offRoadDestinationReachedDelegateAA03OffdefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadDestinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC33offRoadDestinationReachedDelegateAA03OffdefG0_pSgvp">offRoadDestinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the arrival at the off-road destination.
Off-road destination reached notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset
the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offRoadDestinationReachedDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC23offRoadProgressDelegateAA03OffdeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadProgressDelegate"></a>
<a class="token" href="#/s:7heresdk9NavigatorC23offRoadProgressDelegateAA03OffdeF0_pSgvp">offRoadProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the off-road progress.
Off-road progress notifications only occurs if a route has been set.
Setting <code>nil</code> value to the delegate will unset
the delegate.
It returns <code>nil</code> when no delegate is set by an user.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offRoadProgressDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27maneuverNotificationOptionsAA08ManeuverdE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverNotificationOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27maneuverNotificationOptionsAA08ManeuverdE0Vvp">maneuverNotificationOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for maneuver notifications.
Notifications are only available if a route is present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverNotificationOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC16eventTextOptionsAA05EventdE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC16eventTextOptionsAA05EventdE0Vvp">eventTextOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for text notifications.
Notifications are only available if a route is present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">eventTextOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-eventtextoptions">EventTextOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC19speedWarningOptionsAA05SpeeddE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningOptions"></a>
<a class="token" href="#/s:7heresdk9NavigatorC19speedWarningOptionsAA05SpeeddE0Vvp">speedWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for the speed warning feature.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-speedwarningoptions">SpeedWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC27isEnableTunnelExtrapolationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEnableTunnelExtrapolation"></a>
<a class="token" href="#/s:7heresdk9NavigatorC27isEnableTunnelExtrapolationSbvp">isEnableTunnelExtrapolation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines whether to enable or disable tunnel extrapolation.
By default the tunnel extrapolation is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isEnableTunnelExtrapolation</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPassthroughWaypointsHandlingEnabled"></a>
<a class="token" href="#/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">isPassthroughWaypointsHandlingEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines whether to enable or disable handling of passthrough waypoints.
By default the handling of passthrough waypoints is disabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPassthroughWaypointsHandlingEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC14trafficOnRouteAA07TrafficdE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficOnRoute"></a>
<a class="token" href="#/s:7heresdk9NavigatorC14trafficOnRouteAA07TrafficdE0VSgvp">trafficOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic information for the current route.
This impacts <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeprogress">RouteProgress</a></code> updates as the duration of the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionprogress">SectionProgress</a></code> might change.
However, the remaining distance and the route geometry will remain unchanged.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficOnRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficonroute">TrafficOnRoute</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC15locationManagerAA08LocationD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/locationManager"></a>
<a class="token" href="#/s:7heresdk9NavigatorC15locationManagerAA08LocationD0Cvp">locationManager</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The location manager used by the navigator for map-matched location processing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">locationManager</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-locationmanager">LocationManager</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC11getManeuver5indexAA0D0CSgs5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuver(index:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC11getManeuver5indexAA0D0CSgs5Int32V_tF">getManeuver(index:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns maneuver at the given index.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getManeuver</span><span class="p">(</span><span class="nv">index</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-maneuver">Maneuver</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>index</em>
</code>
</td>
<td>
<div>
<p>The index of maneuver requested.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The maneuver if it exists or otherwise <code>nil</code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0defG0VAA09TransportI0O_AA0fK0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuverNotificationTimingOptions(transportMode:timingProfile:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0defG0VAA09TransportI0O_AA0fK0OtF">getManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes
of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function
for the same combination of transport mode and timing profile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getManeuverNotificationTimingOptions</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">timingProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-timingprofile">TimingProfile</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>transportMode</em>
</code>
</td>
<td>
<div>
<p>The transport mode of the timing options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>timingProfile</em>
</code>
</td>
<td>
<div>
<p>The timing profile of the timing options.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The timing options with default values.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportI0O_AA0fK0OAA0defG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setManeuverNotificationTimingOptions(transportMode:timingProfile:options:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportI0O_AA0fK0OAA0defG0VtF">setManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set timing option values for the combination of transport mode and timing profile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">setManeuverNotificationTimingOptions</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">timingProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-timingprofile">TimingProfile</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>transportMode</em>
</code>
</td>
<td>
<div>
<p>The transport mode of the timing options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>timingProfile</em>
</code>
</td>
<td>
<div>
<p>The timing profile of the timing options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The timing options.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if set successfully, <code>false</code> when options has invalid value, see <code><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></code> for
more details about options.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC31getWarningNotificationDistances11warningTypeAA0deF0VAA0dH0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarningNotificationDistances(warningType:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC31getWarningNotificationDistances11warningTypeAA0deF0VAA0dH0O_tF">getWarningNotificationDistances(warningType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the warning notification distances for the requested warning type. The return value can be used as the
base for configuring warning notification distances. Configure the relevant attributes of this object according
to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
warning type and the modified warning notification distances object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-warningtype">WarningType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-warningnotificationdistances">WarningNotificationDistances</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningType</em>
</code>
</td>
<td>
<div>
<p>The warning type for which the notification distances will be returned.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The notification distances for the given warning type.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC31setWarningNotificationDistances11warningType0geF0SbAA0dH0O_AA0deF0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWarningNotificationDistances(warningType:warningNotificationDistances:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC31setWarningNotificationDistances11warningType0geF0SbAA0dH0O_AA0deF0VtF">setWarningNotificationDistances(warningType:<wbr/>warningNotificationDistances:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set the warning notification distances for the specified warning types.
<strong>Note:</strong> The warning notification distances are set for most warners.
This method can’t be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code><a href="sdk-for-ios-navigate-api-reference-..-enums-timingprofile">TimingProfile</a></code>.
If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code><a href="sdk-for-ios-navigate-api-reference-..-enums-timingprofile">TimingProfile</a></code>.
Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">setWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-warningtype">WarningType</a></span><span class="p">,</span> <span class="nv">warningNotificationDistances</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-warningnotificationdistances">WarningNotificationDistances</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningType</em>
</code>
</td>
<td>
<div>
<p>The warning type for which the warning notification distances will be set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>warningNotificationDistances</em>
</code>
</td>
<td>
<div>
<p>The warning notification distances to be set for the specified warning types.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if set successfully, <code>false</code> when the warning_type is [WarningType.SCHOOL_ZONE] or the options have invalid values,
see <code><a href="sdk-for-ios-navigate-api-reference-..-structs-warningnotificationdistances">WarningNotificationDistances</a></code> for more details about warning notification distances.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC30repeatLastManeuverNotificationyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/repeatLastManeuverNotification()"></a>
<a class="token" href="#/s:7heresdk9NavigatorC30repeatLastManeuverNotificationyyF">repeatLastManeuverNotification()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">repeatLastManeuverNotification</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRemainingDistanceInMeters(coordinates:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF">calculateRemainingDistanceInMeters(coordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method calculates the distance between the current position and given coordinates.
The coordinates must be on the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRemainingDistanceInMeters</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The geographic coordinates of the location.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>distance in meters or null if given coordinates are not on route or given
coordinates were already traversed.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC15setCustomOption3key5valueySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(key:value:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC15setCustomOption3key5valueySS_SStF">setCustomOption(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method sets custom options that controls navigator behavior.
Unsupported options are silently ignored.
Undocumented options can change their meaning without going through deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomOption</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>Option name</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>New option value</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC17onLocationUpdatedyyAA0D0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk9NavigatorC17onLocationUpdatedyyAA0D0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code>Navigator</code> or <code><a href="sdk-for-ios-navigate-api-reference-..-classes-visualnavigator">VisualNavigator</a></code>,
it’s required to set the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter for each <code><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></code>
object so that the HERE SDK can map-match the locations properly.
If the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></code> object.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>location</em>
</code>
</td>
<td>
<div>
<p>Current location.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/availableLanguagesForManeuverNotifications()"></a>
<a class="token" href="#/s:7heresdk9NavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ">availableLanguagesForManeuverNotifications()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the list of languages for maneuver notification currently available in the SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">availableLanguagesForManeuverNotifications</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-languagecode">LanguageCode</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>the list of languages for maneuver notification currently available in the SDK.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
