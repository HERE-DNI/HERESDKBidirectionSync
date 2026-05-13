---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-visualnavigator"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VisualNavigator.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VisualNavigator"></a>
<a title="VisualNavigator Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VisualNavigator Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VisualNavigator</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VisualNavigator</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides all functionality of <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code>. In addition,
it provides advanced rendering capabilities for a smooth navigation experience.
This includes interpolation of location updates along a route during turn-by-turn navigation
and during tracking mode. By default, suitable map view settings are automatically applied.
For example, a predefined current location marker is rendered.
Similar to <code><a href="sdk-for-ios-navigate-api-reference-..-classes-navigator">Navigator</a></code>, this class continuously reacts to new locations
provided from a location source and acts as a <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-locationdelegate">LocationDelegate</a></code>.
Note that the VisualNavigator takes control of the MapView’s (maximum) frame rate when rendering,
i.e., between <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">VisualNavigator.startRendering(...)</a></code> and <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC13stopRenderingyyF">VisualNavigator.stopRendering(...)</a></code> calls. It overwrites the MapView’s frame
rate when some camera behavior is set using the <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp">VisualNavigator.guidanceFrameRate</a></code>. When no camera behavior
is preset, the original MapView’s frame rate (the value prior to the <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">VisualNavigator.startRendering(...)</a></code> call) will
be used. While the VisualNavigator is rendering, direct changes in the MapView’s frame rate can
lead to unexpected behavior and therefore should be avoided.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorCACyKcfc">init()</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when operation fails.

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
<a name="/s:7heresdk15VisualNavigatorC9sdkEngineAcA09SDKNativeE0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC9sdkEngineAcA09SDKNativeE0C_tKcfc">init(sdkEngine:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when operation fails.

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
<p>An SDKEngine instance.</p>
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
<a name="/s:7heresdk15VisualNavigatorC9navigatorAcA0C8Protocol_p_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(navigator:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC9navigatorAcA0C8Protocol_p_tKcfc">init(navigator:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class using provided instance of <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code> as source of data.</p>
<p><strong>Note:</strong> The <code>VisualNavigator</code> implements the <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code> interface and forwards
all calls to the underlying <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code> instance. When multiple <code>VisualNavigator</code>
instances share the same <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code> instance, method calls on this common instance
will overwrite changes made by another, which may lead to unexpected behavior.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when operation fails.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">navigator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>navigator</em>
</code>
</td>
<td>
<div>
<p>A NavigatorInterface implementation instance.</p>
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
<a name="/s:7heresdk15VisualNavigatorC9sdkEngine9navigatorAcA09SDKNativeE0C_AA0C8Protocol_ptKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:navigator:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC9sdkEngine9navigatorAcA09SDKNativeE0C_AA0C8Protocol_ptKcfc">init(sdkEngine:<wbr/>navigator:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class using provided instance of <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></code> as source of data.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when operation fails.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">navigator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-navigatorprotocol">NavigatorProtocol</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>An SDKEngine instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>navigator</em>
</code>
</td>
<td>
<div>
<p>A NavigatorInterface implementation instance.</p>
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
<a name="/s:7heresdk15VisualNavigatorC5routeAA5RouteCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/route"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC5routeAA5RouteCSgvp">route</a>
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
<a name="/s:7heresdk15VisualNavigatorC24trackingTransportProfileAA0eF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportProfile"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC24trackingTransportProfileAA0eF0VSgvp">trackingTransportProfile</a>
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
<a name="/s:7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trackingTransportSpecification"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp">trackingTransportSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the transport specification for the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-navigator">Navigator</a></code>, when no route is present.
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
<a name="/s:7heresdk15VisualNavigatorC25navigableLocationDelegateAA09NavigableeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/navigableLocationDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC25navigableLocationDelegateAA09NavigableeF0_pSgvp">navigableLocationDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC21routeProgressDelegateAA05RouteeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeProgressDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC21routeProgressDelegateAA05RouteeF0_pSgvp">routeProgressDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC22routeDeviationDelegateAA05RouteeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeDeviationDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC22routeDeviationDelegateAA05RouteeF0_pSgvp">routeDeviationDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC17eventTextDelegateAA05EventeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC17eventTextDelegateAA05EventeF0_pSgvp">eventTextDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC23milestoneStatusDelegateAA09MilestoneeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/milestoneStatusDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23milestoneStatusDelegateAA09MilestoneeF0_pSgvp">milestoneStatusDelegate</a>
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
but can be included via <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">isPassthroughWaypointsHandlingEnabled</a></code>.
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
<a name="/s:7heresdk15VisualNavigatorC26destinationReachedDelegateAA011DestinationeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/destinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC26destinationReachedDelegateAA011DestinationeF0_pSgvp">destinationReachedDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC20speedWarningDelegateAA05SpeedeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC20speedWarningDelegateAA05SpeedeF0_pSgvp">speedWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp">maneuverViewLaneAssistanceDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentSituationLaneAssistanceViewDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp">currentSituationLaneAssistanceViewDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/environmentalZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp">environmentalZoneWarningListenerDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp">junctionViewLaneAssistanceDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp">safetyCameraWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC26safetyCameraWarningOptionsAA06SafetyefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/safetyCameraWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC26safetyCameraWarningOptionsAA06SafetyefG0Vvp">safetyCameraWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dangerZoneWarningListenerDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp">dangerZoneWarningListenerDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp">truckRestrictionsWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC12warnerEngineAA06WarnerE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warnerEngine"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC12warnerEngineAA06WarnerE0Cvp">warnerEngine</a>
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
<a name="/s:7heresdk15VisualNavigatorC31truckRestrictionsWarningOptionsAA05TruckefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckRestrictionsWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC31truckRestrictionsWarningOptionsAA05TruckefG0Vvp">truckRestrictionsWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC18postActionDelegateAA04PosteF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postActionDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC18postActionDelegateAA04PosteF0_pSgvp">postActionDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC18speedLimitDelegateAA05SpeedeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC18speedLimitDelegateAA05SpeedeF0_pSgvp">speedLimitDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC17roadTextsDelegateAA04RoadeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadTextsDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC17roadTextsDelegateAA04RoadeF0_pSgvp">roadTextsDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC22roadAttributesDelegateAA04RoadeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadAttributesDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC22roadAttributesDelegateAA04RoadeF0_pSgvp">roadAttributesDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC23roadSignWarningDelegateAA04RoadefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23roadSignWarningDelegateAA04RoadefG0_pSgvp">roadSignWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC22roadSignWarningOptionsAA04RoadefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC22roadSignWarningOptionsAA04RoadefG0Vvp">roadSignWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp">schoolZoneWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC24schoolZoneWarningOptionsAA06SchoolefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/schoolZoneWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC24schoolZoneWarningOptionsAA06SchoolefG0Vvp">schoolZoneWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC28realisticViewWarningDelegateAA09RealisticefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC28realisticViewWarningDelegateAA09RealisticefG0_pSgvp">realisticViewWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC27realisticViewWarningOptionsAA09RealisticefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27realisticViewWarningOptionsAA09RealisticefG0Vvp">realisticViewWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC29borderCrossingWarningDelegateAA06BorderefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC29borderCrossingWarningDelegateAA06BorderefG0_pSgvp">borderCrossingWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC28borderCrossingWarningOptionsAA06BorderefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/borderCrossingWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC28borderCrossingWarningOptionsAA06BorderefG0Vvp">borderCrossingWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC23tollStopWarningDelegateAA04TollefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollStopWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23tollStopWarningDelegateAA04TollefG0_pSgvp">tollStopWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp">railwayCrossingWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lowSpeedZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp">lowSpeedZoneWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp">trafficMergeWarningDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC26trafficMergeWarningOptionsAA07TrafficefG0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficMergeWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC26trafficMergeWarningOptionsAA07TrafficefG0Vvp">trafficMergeWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadDestinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp">offRoadDestinationReachedDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC23offRoadProgressDelegateAA03OffefG0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoadProgressDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23offRoadProgressDelegateAA03OffefG0_pSgvp">offRoadProgressDelegate</a>
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
<a name="/s:7heresdk15VisualNavigatorC27maneuverNotificationOptionsAA08ManeuvereF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverNotificationOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27maneuverNotificationOptionsAA08ManeuvereF0Vvp">maneuverNotificationOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC16eventTextOptionsAA05EventeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eventTextOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC16eventTextOptionsAA05EventeF0Vvp">eventTextOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC19speedWarningOptionsAA05SpeedeF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedWarningOptions"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC19speedWarningOptionsAA05SpeedeF0Vvp">speedWarningOptions</a>
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
<a name="/s:7heresdk15VisualNavigatorC27isEnableTunnelExtrapolationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEnableTunnelExtrapolation"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27isEnableTunnelExtrapolationSbvp">isEnableTunnelExtrapolation</a>
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
<a name="/s:7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPassthroughWaypointsHandlingEnabled"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">isPassthroughWaypointsHandlingEnabled</a>
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
<a name="/s:7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficOnRoute"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp">trafficOnRoute</a>
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
<a name="/s:7heresdk15VisualNavigatorC15locationManagerAA08LocationE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/locationManager"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC15locationManagerAA08LocationE0Cvp">locationManager</a>
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
<a name="/s:7heresdk15VisualNavigatorC14cameraBehaviorAA06CameraE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraBehavior"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC14cameraBehaviorAA06CameraE0_pSgvp">cameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera behavior which defines how the <code>VisualNavigator</code> handles the camera.
Setting <code>nil</code> disables any camera behavior with the result that the camera does not follow
the current location and keeps the last active camera state, i.e., current zoom and tilt.
Furthermore, when <code>nil</code> is set map gestures can be used again to freely pan and zoom
the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
zoomed by the user.
The default value is an instance of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-fixedcamerabehavior">FixedCameraBehavior</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraBehavior</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-camerabehavior">CameraBehavior</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC14isRouteVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRouteVisible"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC14isRouteVisibleSbvp">isRouteVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></code> visibility which defines whether to perform route rendering during visual navigation.
When enabled, the set <code><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></code> will be rendered as a <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mappolyline">MapPolyline</a></code> together with <code><a href="sdk-for-ios-navigate-api-reference-..-classes-maparrow">MapArrow</a></code> items that
indicate the next turns. By default, it is enabled.
When disabled, <code><a href="sdk-for-ios-navigate-api-reference-..-classes-maparrow">MapArrow</a></code> items are still rendered. To hide arrows, use <code><a href="sdk-for-ios-navigate-api-reference-..-classes-visualnavigatorcolors">VisualNavigatorColors</a></code> with
transparent color.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRouteVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC22isRouteProgressVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRouteProgressVisible"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC22isRouteProgressVisibleSbvp">isRouteProgressVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeprogress">RouteProgress</a></code> visibility which defines whether to perform route progress coloring (“eat-up”) during visual navigation.
By default, it is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRouteProgressVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC23isManeuverArrowsVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isManeuverArrowsVisible"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23isManeuverArrowsVisibleSbvp">isManeuverArrowsVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation.
By default, it is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isManeuverArrowsVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC27isOffRoadDestinationVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isOffRoadDestinationVisible"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC27isOffRoadDestinationVisibleSbvp">isOffRoadDestinationVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination
which is off-road. By default it is enabled.
<strong>Note:</strong> The dashed line will be drawn only if the original destination is off-road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isOffRoadDestinationVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC23isTrafficOnRouteVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTrafficOnRouteVisible"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23isTrafficOnRouteVisibleSbvp">isTrafficOnRouteVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></code> visualization
is enabled during visual navigation.
When enabled the route’s <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mappolyline">MapPolyline</a></code> will be enhanced with visualization of the traffic conditions.
Colors used for this visualization are defined in <code><a href="../Classes/VisualNavigatorColors.html#/s:7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp">VisualNavigatorColors.trafficOnRouteColors</a></code>.
The presented traffic information is either set by the user via <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp">trafficOnRoute</a></code> or
is generated from historical traffic data stored in the map.
<strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
through the [sdk.routing.RoutingEngine.calculate_traffic_on_route] interface. The returned <code><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficonroute">TrafficOnRoute</a></code>
could then be used to update [sdk.navigation.NavigatorInterface.traffic_on_route] to refresh the traffic on route visualization.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTrafficOnRouteVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customLocationIndicator"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp">customLocationIndicator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Custom location indicator <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationindicator">LocationIndicator</a></code> which <code>VisualNavigator</code> uses instead of the default.
If set, the user is responsible for adding and removing the object to/from the mapview.
It is important to stop sending location updates to the provided <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationindicator">LocationIndicator</a></code>, since
<code>VisualNavigator</code> will control its position when rendering is active, i.e., between startRendering(<em>) and
stopRendering() calls. By default this property is <code>nil</code>,
which means the default indicator is used, and <code>VisualNavigator</code> automatically adds and removes it to/from
the mapview upon startRendering(</em>) and stopRendering() calls.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customLocationIndicator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-locationindicator">LocationIndicator</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC28interpolatedLocationDelegateAA012InterpolatedeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/interpolatedLocationDelegate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC28interpolatedLocationDelegateAA012InterpolatedeF0_pSgvp">interpolatedLocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object to receive interpolated locations.
For example, to pan a second instance of a <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewbase">MapViewBase</a></code> or move additional markers smoothly.
The map-matched locations are used if available, otherwise the non-map-matched ones are used instead.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">interpolatedLocationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-interpolatedlocationdelegate">InterpolatedLocationDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC11isRenderingSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRendering"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC11isRenderingSbvp">isRendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a value indicating whether visual navigation rendering is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRendering</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC6colorsAA0bC6ColorsCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/colors"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC6colorsAA0bC6ColorsCvp">colors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Object containing colors used to render route progress and maneuver arrow visualization.
Setting a new instance overwrites the default color settings as specified in <code><a href="sdk-for-ios-navigate-api-reference-..-classes-visualnavigatorcolors">VisualNavigatorColors</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">colors</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-visualnavigatorcolors">VisualNavigatorColors</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/measureDependentWidth"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp">measureDependentWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.
It is a dictionary that has keys that are <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>s and values
that are width in pixels at this <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>s.
This route and maneuver arrows width is multiplied by a pixel_scale <code>pixelScale</code>
before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
<code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp">VisualNavigator.maneuverArrowWidthFactor</a></code>; which by default equals one.
The function defined by a dictionary is linearly interpolated between each successive pair of data points.
For keys below the lowest <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>, its corresponding value width is used.
For keys above the highest <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>, its corresponding value width is used.
Only <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code> of [sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL] type are supported.
<code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code> of other unsupported types will be ignored.
<code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
value of this single entry for all <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>s.
Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
If route and maneuver arrows were not configured with this property,
then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">measureDependentWidth</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverArrowWidthFactor"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp">maneuverArrowWidthFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A factor of <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp">VisualNavigator.measureDependentWidth</a></code> defining the width of the maneuver arrow.
The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverArrowWidthFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC22isExtrapolationEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isExtrapolationEnabled"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC22isExtrapolationEnabledSbvp">isExtrapolationEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines whether the position extrapolation logic is enabled or not.
The predicted location follows the geometry of the route (or road) ahead.
By default it is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isExtrapolationEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC16debugGpxFilePathSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/debugGpxFilePath"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC16debugGpxFilePathSSSgvp">debugGpxFilePath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Show the contents of a GPX file on the map.
<strong>Note:</strong> This API should be used for debugging purposes only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">debugGpxFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC18isDebugModeEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDebugModeEnabled"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC18isDebugModeEnabledSbvp">isDebugModeEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When enabled, it shows useful information for debugging purposes.</p>
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
</ul></li>
</ul>
<p>Fields between brackets ([]‘s) are omitted if not available.</p>
<p>Example:</p>
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
<p><strong>Note:</strong> This API should be used for debugging purposes only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDebugModeEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC28isLocationAccuracyVisualizedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isLocationAccuracyVisualized"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC28isLocationAccuracyVisualizedSbvp">isLocationAccuracyVisualized</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls if the halo accuracy visualization of the default <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationindicator">LocationIndicator</a></code> is rendered or not.
Does not affect halo accuracy indicator of the <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp">VisualNavigator.customLocationIndicator</a></code>.
If <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp">VisualNavigator.customLocationIndicator</a></code> is set, then its halo accuracy indicator can be controlled
using <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp">LocationIndicator.isAccuracyVisualized</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isLocationAccuracyVisualized</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC25isDynamicFrameRateEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDynamicFrameRateEnabled"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC25isDynamicFrameRateEnabledSbvp">isDynamicFrameRateEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Flag used to enable or disable the dynamic frame rate.
Controls whether the number of map updates is dynamically calculated based on
the current zoom level. If the zoom level is low, i.e., the camera target distance is high,
updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will
happen less frequent. It is on by default.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDynamicFrameRateEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/guidanceFrameRate"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp">guidanceFrameRate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Frame rate used during guidance.
Frame rate used during guidance.
Default is 30fps.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">guidanceFrameRate</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC14routeDrawOrders5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeDrawOrder"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC14routeDrawOrders5Int32Vvp">routeDrawOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order of the polylines representing the route.
The draw order of the polylines representing the route. For more details see
<code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC9drawOrders5Int32Vvp">MapPolyline.drawOrder</a></code>.
The default is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeDrawOrder</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC18routeDrawOrderTypeAA0efG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeDrawOrderType"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC18routeDrawOrderTypeAA0efG0Ovp">routeDrawOrderType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order type of the polylines representing the route.
The draw order type of the polylines representing the route. For more details
see <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp">MapPolyline.drawOrderType</a></code>.
The default is <code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeDrawOrderType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-drawordertype">DrawOrderType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC11getManeuver5indexAA0E0CSgs5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuver(index:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC11getManeuver5indexAA0E0CSgs5Int32V_tF">getManeuver(index:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuverNotificationTimingOptions(transportMode:timingProfile:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF">getManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setManeuverNotificationTimingOptions(transportMode:timingProfile:options:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF">setManeuverNotificationTimingOptions(transportMode:<wbr/>timingProfile:<wbr/>options:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarningNotificationDistances(warningType:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF">getWarningNotificationDistances(warningType:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWarningNotificationDistances(warningType:warningNotificationDistances:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF">setWarningNotificationDistances(warningType:<wbr/>warningNotificationDistances:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC30repeatLastManeuverNotificationyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/repeatLastManeuverNotification()"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC30repeatLastManeuverNotificationyyF">repeatLastManeuverNotification()</a>
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
<a name="/s:7heresdk15VisualNavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRemainingDistanceInMeters(coordinates:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF">calculateRemainingDistanceInMeters(coordinates:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC15setCustomOption3key5valueySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(key:value:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC15setCustomOption3key5valueySS_SStF">setCustomOption(key:<wbr/>value:<wbr/>)</a>
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
<a name="/s:7heresdk15VisualNavigatorC17onLocationUpdatedyyAA0E0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC17onLocationUpdatedyyAA0E0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-navigator">Navigator</a></code> or <code>VisualNavigator</code>,
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
<a name="/s:7heresdk15VisualNavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/availableLanguagesForManeuverNotifications()"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ">availableLanguagesForManeuverNotifications()</a>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startRendering(mapView:)"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">startRendering(mapView:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts visual navigation rendering.
A preconfigured current location marker is shown as soon as a location is received.
The marker is chosen according to the transport mode specified in the route. If no route is
present, the marker is chosen based on the <code><a href="../Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp">trackingTransportSpecification</a></code> property.
Calling startRendering(_) changes the <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC14principalPointAA7Point2DVvp">MapCamera.principalPoint</a></code> property so that the current
position indicator is equal to the value from [sdk.navigation.CameraBehavior.normalized_principal_point],
in which by default places the principal point slightly at the bottom of the mapview. It is
restored to its original value when stopRendering() is called.
<strong>Note:</strong> When rendering is started again for a new map view instance, rendering
is automatically stopped on the previous map view instance. Also note that
the <code>frameRate</code> can be lowered to reduce CPU usage, to adjust for tradeoffs
between rendering smoothness versus battery consumption.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startRendering</span><span class="p">(</span><span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>The map view on which visual navigation will take place.</p>
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
<a name="/s:7heresdk15VisualNavigatorC13stopRenderingyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stopRendering()"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC13stopRenderingyyF">stopRendering()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops visual navigation rendering. This removes the current location marker. Other
settings, like map orientation or camera distance, which may have been altered during rendering
are no longer updated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stopRendering</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC47defaultRouteManeuverArrowMeasureDependentWidthsSDyAA03MapH0VSdGyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/defaultRouteManeuverArrowMeasureDependentWidths()"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC47defaultRouteManeuverArrowMeasureDependentWidthsSDyAA03MapH0VSdGyFZ">defaultRouteManeuverArrowMeasureDependentWidths()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves a dictionary of default route and maneuver arrow widths as a function of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>s.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">defaultRouteManeuverArrowMeasureDependentWidths</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A dictionary of default route and maneuver arrow widths as a function of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></code>s.</p>
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
