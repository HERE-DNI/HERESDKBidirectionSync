---
title: "DynamicRoutingDelegate"
slug: "sdk-for-ios-navigate-api-reference-protocols-dynamicroutingdelegate"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DynamicRoutingDelegate"></a>
<a title="DynamicRoutingDelegate Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        DynamicRoutingDelegate Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DynamicRoutingDelegate</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DynamicRoutingDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>This protocol should be implemented in order to
receive notifications about the new route via the <code><a href="sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine">DynamicRoutingEngine</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22DynamicRoutingDelegateP18onBetterRouteFound03newG022etaDifferenceInSeconds08distancekL6MetersyAA0G0C_s5Int32VAKtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onBetterRouteFound(newRoute:etaDifferenceInSeconds:distanceDifferenceInMeters:)"></a>
<a class="token" href="#/s:7heresdk22DynamicRoutingDelegateP18onBetterRouteFound03newG022etaDifferenceInSeconds08distancekL6MetersyAA0G0C_s5Int32VAKtF">onBetterRouteFound(newRoute:<wbr/>etaDifferenceInSeconds:<wbr/>distanceDifferenceInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This event is issued when a better route could be found,
as defined by <code><a href="sdk-for-ios-navigate-api-reference-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></code>.
To find a better route, two routes are calculated.
The updated current route: A route that is calculated via the route specified.
The dynamic route: A route that starts at the current position on the route specified
and passes through the remaining waypoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onBetterRouteFound</span><span class="p">(</span><span class="nv">newRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></span><span class="p">,</span> <span class="nv">etaDifferenceInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">distanceDifferenceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>newRoute</em>
</code>
</td>
<td>
<div>
<p>The newly calculated route with the remaining waypoints starting from the
current location.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>etaDifferenceInSeconds</em>
</code>
</td>
<td>
<div>
<p>The difference in seconds:
eta of the current updated route - eta of the dynamic route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>distanceDifferenceInMeters</em>
</code>
</td>
<td>
<div>
<p>The difference in meters:
distance of the current updated route - distance of the dynamic route.
The value can be negative in case the current updated route has
a shorter distance, but its now assumed to be longer than the dynamic route.</p>
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
<a name="/s:7heresdk22DynamicRoutingDelegateP02onC5Error07routingF0yAA0cF0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onRoutingError(routingError:)"></a>
<a class="token" href="#/s:7heresdk22DynamicRoutingDelegateP02onC5Error07routingF0yAA0cF0O_tF">onRoutingError(routingError:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This event is issued when an error occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onRoutingError</span><span class="p">(</span><span class="nv">routingError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routingerror">RoutingError</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routingError</em>
</code>
</td>
<td>
<div>
<p>Routing error</p>
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
