---
title: "PedestrianOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-pedestrianoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PedestrianOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/PedestrianOptions"></a>
<a title="PedestrianOptions Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PedestrianOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")
public struct PedestrianOptions : Hashable</code></pre>
</div>
</div>
<p>All the options to specify how a pedestrian route should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the common route calculation options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var routeOptions: RouteOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Customize textual content returned from the route calculation, such
as localization, format, and unit system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var textOptions: RouteTextOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify restrictions for route calculations. By default
no restrictions are applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var avoidanceOptions: AvoidanceOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV26walkSpeedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/walkSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV26walkSpeedInMetersPerSecondSdvp">walkSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the speed that will be used by the service as the walking speed
for pedestrian routing in meters per second. It influences the duration of
walking segments along the route. The provided value must be in the range
[0.5, 2.0]. When the value is outside this range, an invalid parameter
error is raised. Refer to <code><a href="../Enums/RoutingError.html">RoutingError</a></code> for details. The default
speed is 1 meter per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var walkSpeedInMetersPerSecond: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV05routeC004textC009avoidanceC026walkSpeedInMetersPerSecondAcA05RouteC0V_AA0m4TextC0VAA09AvoidanceC0VSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:walkSpeedInMetersPerSecond:)"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV05routeC004textC009avoidanceC026walkSpeedInMetersPerSecondAcA05RouteC0V_AA0m4TextC0VAA09AvoidanceC0VSdtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>walkSpeedInMetersPerSecond:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), walkSpeedInMetersPerSecond: Double = 1.0)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianOptionsV33fromDefaultParameterConfigurationACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromDefaultParameterConfiguration()"></a>
<a class="token" href="#/s:7heresdk17PedestrianOptionsV33fromDefaultParameterConfigurationACyFZ">fromDefaultParameterConfiguration()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns PedestrianOptions instance with default values used in SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func fromDefaultParameterConfiguration() -&gt; PedestrianOptions</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A <code>PedestrianOptions</code> instance with default values used in SDK.</p>
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



</div>
`
}</HTMLBlock>
