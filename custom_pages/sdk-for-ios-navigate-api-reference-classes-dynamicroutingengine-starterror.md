---
title: "StartError"
slug: "sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine-starterror"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/StartError"></a>
<a title="StartError Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

<a href="sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine">DynamicRoutingEngine</a>

        StartError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>StartError</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">StartError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine">DynamicRoutingEngine</a></span><span class="o">.</span><span class="kt">StartError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Start error</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO08internalF0yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalError"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO08internalF0yA2EmF">internalError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An internal issue occurred.
Maybe the logs can provide some information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO12missingRouteyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/missingRoute"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO12missingRouteyA2EmF">missingRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The passed route object is invalid/<code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">missingRoute</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO18missingRouteHandleyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/missingRouteHandle"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO18missingRouteHandleyA2EmF">missingRouteHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The passed route has no route handle.
<code><a href="../../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">RouteOptions.enableRouteHandle</a></code> needs to be set to true
on the initial route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">missingRouteHandle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO15missingListeneryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/missingListener"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO15missingListeneryA2EmF">missingListener</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The listener is not valid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">missingListener</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO15tooFewWaypointsyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tooFewWaypoints"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO15tooFewWaypointsyA2EmF">tooFewWaypoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Too few waypoints where passed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tooFewWaypoints</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO26invalidRefreshRouteOptionsyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidRefreshRouteOptions"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO26invalidRefreshRouteOptionsyA2EmF">invalidRefreshRouteOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid RefreshRouteOptions passed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidRefreshRouteOptions</span></code></pre>
</div>
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
