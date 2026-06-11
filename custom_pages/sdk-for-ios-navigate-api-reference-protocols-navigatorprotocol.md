---
title: "NavigatorProtocol"
slug: "sdk-for-ios-navigate-api-reference-protocols-navigatorprotocol"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/NavigatorProtocol"></a>
<a title="NavigatorProtocol Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        NavigatorProtocol Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>NavigatorProtocol</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">NavigatorProtocol</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
</div>
</div>
<p>This protocol provides the basic functionality needed to run a navigation session.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP5routeAA5RouteCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/route"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP5routeAA5RouteCSgvp">route</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route to navigate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP24trackingTransportProfileAA0eF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportProfile"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP24trackingTransportProfileAA0eF0VSgvp">trackingTransportProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the transport profile for the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code>, when no route is present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")</span>
<span class="k">var</span> <span class="nv">trackingTransportProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportprofile">TransportProfile</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP30trackingTransportSpecificationAA0eF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportSpecification"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP30trackingTransportSpecificationAA0eF0VSgvp">trackingTransportSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the transport specification for the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code>, when no route is present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">trackingTransportSpecification</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP25navigableLocationDelegateAA09NavigableeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/navigableLocationDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP25navigableLocationDelegateAA09NavigableeF0_pSgvp">navigableLocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">navigableLocationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-navigablelocationdelegate">NavigableLocationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP21routeProgressDelegateAA05RouteeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeProgressDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP21routeProgressDelegateAA05RouteeF0_pSgvp">routeProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about navigation route progress.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">routeProgressDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-routeprogressdelegate">RouteProgressDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP22routeDeviationDelegateAA05RouteeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeDeviationDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP22routeDeviationDelegateAA05RouteeF0_pSgvp">routeDeviationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about deviations from the route if any occurs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">routeDeviationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-routedeviationdelegate">RouteDeviationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP17eventTextDelegateAA05EventeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP17eventTextDelegateAA05EventeF0_pSgvp">eventTextDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive text notifications when they are available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">eventTextDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-eventtextdelegate">EventTextDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP23milestoneStatusDelegateAA09MilestoneeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/milestoneStatusDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP23milestoneStatusDelegateAA09MilestoneeF0_pSgvp">milestoneStatusDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the arrival at each <code><a href="sdk-for-ios-navigate-api-reference-structs-milestone">Milestone</a></code> or missing it.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">milestoneStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP26destinationReachedDelegateAA011DestinationeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/destinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP26destinationReachedDelegateAA011DestinationeF0_pSgvp">destinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the arrival at the destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">destinationReachedDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-destinationreacheddelegate">DestinationReachedDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP20speedWarningDelegateAA05SpeedeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP20speedWarningDelegateAA05SpeedeF0_pSgvp">speedWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">speedWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-speedwarningdelegate">SpeedWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp">maneuverViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive maneuver view lane assistance notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">maneuverViewLaneAssistanceDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentSituationLaneAssistanceViewDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp">currentSituationLaneAssistanceViewDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive current situation lane assistance view notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">currentSituationLaneAssistanceViewDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/environmentalZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp">environmentalZoneWarningListenerDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notification on approaching environmental zones.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">environmentalZoneWarningListenerDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp">junctionViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive junction view lane assistance notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">junctionViewLaneAssistanceDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp">safetyCameraWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive safety camera warner notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">safetyCameraWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP26safetyCameraWarningOptionsAA06SafetyefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP26safetyCameraWarningOptionsAA06SafetyefG0Vvp">safetyCameraWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera warning options to be passed to <code><a href="sdk-for-ios-navigate-api-reference-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">safetyCameraWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dangerZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp">dangerZoneWarningListenerDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notification on approaching danger zones.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">dangerZoneWarningListenerDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp">truckRestrictionsWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about truck restrictions on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">truckRestrictionsWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP12warnerEngineAA06WarnerE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warnerEngine"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP12warnerEngineAA06WarnerE0Cvp">warnerEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Warner engine used by the navigator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">warnerEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-warnerengine">WarnerEngine</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP31truckRestrictionsWarningOptionsAA05TruckefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP31truckRestrictionsWarningOptionsAA05TruckefG0Vvp">truckRestrictionsWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <code><a href="sdk-for-ios-navigate-api-reference-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">truckRestrictionsWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP18postActionDelegateAA04PosteF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postActionDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP18postActionDelegateAA04PosteF0_pSgvp">postActionDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive post action notifications, such as a charge action at a charging station.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">postActionDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-postactiondelegate">PostActionDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP18speedLimitDelegateAA05SpeedeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP18speedLimitDelegateAA05SpeedeF0_pSgvp">speedLimitDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the speed limit of the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">speedLimitDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-speedlimitdelegate">SpeedLimitDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP17roadTextsDelegateAA04RoadeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadTextsDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP17roadTextsDelegateAA04RoadeF0_pSgvp">roadTextsDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about the textual attributes of the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">roadTextsDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-roadtextsdelegate">RoadTextsDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP22roadAttributesDelegateAA04RoadeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadAttributesDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP22roadAttributesDelegateAA04RoadeF0_pSgvp">roadAttributesDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about attributes of the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">roadAttributesDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-roadattributesdelegate">RoadAttributesDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP23roadSignWarningDelegateAA04RoadefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP23roadSignWarningDelegateAA04RoadefG0_pSgvp">roadSignWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about road signs on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">roadSignWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP22roadSignWarningOptionsAA04RoadefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP22roadSignWarningOptionsAA04RoadefG0Vvp">roadSignWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road sign warning options that allow to filter road sings to be passed to <code><a href="sdk-for-ios-navigate-api-reference-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">roadSignWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-roadsignwarningoptions">RoadSignWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp">schoolZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about school zones on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">schoolZoneWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP24schoolZoneWarningOptionsAA06SchoolefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP24schoolZoneWarningOptionsAA06SchoolefG0Vvp">schoolZoneWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>School zone warning options</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">schoolZoneWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP28realisticViewWarningDelegateAA09RealisticefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP28realisticViewWarningDelegateAA09RealisticefG0_pSgvp">realisticViewWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about junction views on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">realisticViewWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27realisticViewWarningOptionsAA09RealisticefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27realisticViewWarningOptionsAA09RealisticefG0Vvp">realisticViewWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Realistic view warning options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">realisticViewWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP29borderCrossingWarningDelegateAA06BorderefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP29borderCrossingWarningDelegateAA06BorderefG0_pSgvp">borderCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about border crossings on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">borderCrossingWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP28borderCrossingWarningOptionsAA06BorderefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP28borderCrossingWarningOptionsAA06BorderefG0Vvp">borderCrossingWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Border crossing warning options to be passed to <code><a href="sdk-for-ios-navigate-api-reference-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a></code>. These options</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">borderCrossingWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP23tollStopWarningDelegateAA04TollefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollStopWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP23tollStopWarningDelegateAA04TollefG0_pSgvp">tollStopWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive information on the upcoming toll stop.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">tollStopWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp">railwayCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about railway crossings on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">railwayCrossingWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lowSpeedZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp">lowSpeedZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about low speed zones on the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">lowSpeedZoneWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp">trafficMergeWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive notifications about merging traffic to the current road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">trafficMergeWarningDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP26trafficMergeWarningOptionsAA07TrafficefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP26trafficMergeWarningOptionsAA07TrafficefG0Vvp">trafficMergeWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
<code><a href="sdk-for-ios-navigate-api-reference-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">trafficMergeWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadDestinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp">offRoadDestinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the arrival at the off-road destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">offRoadDestinationReachedDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP23offRoadProgressDelegateAA03OffefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadProgressDelegate"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP23offRoadProgressDelegateAA03OffefG0_pSgvp">offRoadProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive the notification about the off-road progress.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">offRoadProgressDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27maneuverNotificationOptionsAA08ManeuvereF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverNotificationOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27maneuverNotificationOptionsAA08ManeuvereF0Vvp">maneuverNotificationOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for maneuver notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">maneuverNotificationOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP16eventTextOptionsAA05EventeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP16eventTextOptionsAA05EventeF0Vvp">eventTextOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for text notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">eventTextOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-eventtextoptions">EventTextOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP19speedWarningOptionsAA05SpeedeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningOptions"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP19speedWarningOptionsAA05SpeedeF0Vvp">speedWarningOptions</a>
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
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">speedWarningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-speedwarningoptions">SpeedWarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP27isEnableTunnelExtrapolationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEnableTunnelExtrapolation"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP27isEnableTunnelExtrapolationSbvp">isEnableTunnelExtrapolation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines whether to enable or disable tunnel extrapolation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">isEnableTunnelExtrapolation</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP37isPassthroughWaypointsHandlingEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPassthroughWaypointsHandlingEnabled"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP37isPassthroughWaypointsHandlingEnabledSbvp">isPassthroughWaypointsHandlingEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines whether to enable or disable handling of passthrough waypoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">isPassthroughWaypointsHandlingEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP14trafficOnRouteAA07TrafficeF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficOnRoute"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP14trafficOnRouteAA07TrafficeF0VSgvp">trafficOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic information for the current route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">trafficOnRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficonroute">TrafficOnRoute</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP15locationManagerAA08LocationE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/locationManager"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP15locationManagerAA08LocationE0Cvp">locationManager</a>
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
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">locationManager</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-locationmanager">LocationManager</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP17onLocationUpdatedyyAA0E0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP17onLocationUpdatedyyAA0E0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code>,
it’s required to set the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code>
object so that the HERE SDK can map-match the locations properly.
If the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code> object.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></span><span class="p">)</span></code></pre>
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
<a name="/s:7heresdk17NavigatorProtocolP11getManeuver5indexAA0E0CSgs5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuver(index:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP11getManeuver5indexAA0E0CSgs5Int32V_tF">getManeuver(index:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getManeuver</span><span class="p">(</span><span class="nv">index</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></span><span class="p">?</span></code></pre>
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
<a name="/s:7heresdk17NavigatorProtocolP36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuverNotificationTimingOptions(transportMode:timingProfile:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF">getManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getManeuverNotificationTimingOptions</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">timingProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></span></code></pre>
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
<a name="/s:7heresdk17NavigatorProtocolP36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setManeuverNotificationTimingOptions(transportMode:timingProfile:options:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF">setManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>options:<wbr/>)</a>
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
<span class="kd">func</span> <span class="nf">setManeuverNotificationTimingOptions</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">timingProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
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
<p><code>True</code> if set successfully, <code>false</code> when options has invalid value, see <code><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></code> for
more details about options.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarningNotificationDistances(warningType:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF">getWarningNotificationDistances(warningType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span></code></pre>
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
<a name="/s:7heresdk17NavigatorProtocolP31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWarningNotificationDistances(warningType:warningNotificationDistances:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF">setWarningNotificationDistances(warningType:<wbr/>warningNotificationDistances:<wbr/>)</a>
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
Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></code>.
If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></code>.
Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">setWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">,</span> <span class="nv">warningNotificationDistances</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
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
see <code><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></code> for more details about warning notification distances.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP30repeatLastManeuverNotificationyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/repeatLastManeuverNotification()"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP30repeatLastManeuverNotificationyyF">repeatLastManeuverNotification()</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">repeatLastManeuverNotification</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRemainingDistanceInMeters(coordinates:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF">calculateRemainingDistanceInMeters(coordinates:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">calculateRemainingDistanceInMeters</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
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
<a name="/s:7heresdk17NavigatorProtocolP15setCustomOption3key5valueySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(key:value:)"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP15setCustomOption3key5valueySS_SStF">setCustomOption(key:<wbr/>value:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">setCustomOption</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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

`
}</HTMLBlock>
