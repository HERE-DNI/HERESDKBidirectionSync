---
title: "sdk-for-ios-navigate-api-reference-classes-mapview"
slug: "sdk-for-ios-navigate-api-reference-classes-mapview"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapView"></a>
<a title="MapView Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapView Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapView</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@IBDesignable</span>
<span class="kd">@objc(HereMapView)</span>
<span class="kd">@MainActor</span>
<span class="kd">open</span> <span class="kd">class</span> <span class="kt">MapView</span> <span class="p">:</span> <span class="kt">UIView</span><span class="p">,</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapviewbase">MapViewBase</a></span></code></pre>
</div>
</div>
<p>A view that displays a map.
Note: Before using this class, <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> must be already initialized.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC22TakeScreenshotCallbacka"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TakeScreenshotCallback"></a>
<a class="token" href="#/s:7heresdk7MapViewC22TakeScreenshotCallbacka">TakeScreenshotCallback</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Callback to be called on retrieval of screenshot.</p>
<div class="aside aside-note">
<p class="aside-title">Note</p>
    In case of any error passed result is null.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TakeScreenshotCallback</span> <span class="o">=</span> <span class="p">(</span><span class="kt">UIImage</span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC0C3PinC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ViewPin"></a>
<a class="token" href="#/s:7heresdk7MapViewC0C3PinC">ViewPin</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class represents a pinned UIView, that means an UIView at a
fixed location on the map.</p>
<p>The pinned view will automatically be repositioned on the screen as the map moves.
There is more performance overhead involved in positioning an view as
compared to a map marker, so for use cases which only require static images,
markers should be used.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapview-viewpin">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ViewPin</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC6cameraAA0B6CameraCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/camera"></a>
<a class="token" href="#/s:7heresdk7MapViewC6cameraAA0B6CameraCvp">camera</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The MapCamera to control the angle of view for the map</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">camera</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcamera">MapCamera</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC8gesturesAA8GesturesCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gestures"></a>
<a class="token" href="#/s:7heresdk7MapViewC8gesturesAA8GesturesCvp">gestures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The gestures control object for setting up the capture of gestures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">gestures</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-gestures">Gestures</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapScene"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp">mapScene</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">mapScene</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapscene">MapScene</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP10mapContextAA0bF0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapContext"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP10mapContextAA0bF0Cvp">mapContext</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">mapContext</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hereMap"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp">hereMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">hereMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-heremap">HereMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC9frameRates5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/frameRate"></a>
<a class="token" href="#/s:7heresdk7MapViewC9frameRates5Int32Vvp">frameRate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum render frame rate in frames per second.
Setting to 0 disables automatic rendering for this view. Setting negative values has no effect.
The default value is 60 frames per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">frameRate</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC12viewportSizeAA6Size2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewportSize"></a>
<a class="token" href="#/s:7heresdk7MapViewC12viewportSizeAA6Size2DVvp">viewportSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the viewport size in physical pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">viewportSize</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-size2d">Size2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC15primaryLanguageAA0E4CodeOSgvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/primaryLanguage"></a>
<a class="token" href="#/s:7heresdk7MapViewC15primaryLanguageAA0E4CodeOSgvpZ">primaryLanguage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The code of the desired primary map display language. If not set
or if the desired language is not supported, then the language
of the displayed region is used, which is the default behaviour.
Applies to all instances of MapView. When changed, triggers
redraw of any visible MapView.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">static</span> <span class="k">var</span> <span class="nv">primaryLanguage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC17secondaryLanguageAA0E4CodeOSgvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/secondaryLanguage"></a>
<a class="token" href="#/s:7heresdk7MapViewC17secondaryLanguageAA0E4CodeOSgvpZ">secondaryLanguage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The code of the desired secondary map display language. If the desired
language is not supported, then the language of the displayed region
is used. If not set, no secondary map language will be used which
is the default behaviour. Applies to all instances of MapView.
When changed, triggers redraw of any visible MapView.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">static</span> <span class="k">var</span> <span class="nv">secondaryLanguage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC13shadowQualityAA06ShadowE0OvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shadowQuality"></a>
<a class="token" href="#/s:7heresdk7MapViewC13shadowQualityAA06ShadowE0OvpZ">shadowQuality</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The shadow quality for all instances of MapView.
The quality controls the size of the shadow maps and the cascade count.
The default shadow quality is {@code ShadowQuality.medium}.
MapViews can request to render shadows by feature.
Enabling shadows has a performance impact and should be considered only for devices with
sufficient performance.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">static</span> <span class="k">var</span> <span class="nv">shadowQuality</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-shadowquality">ShadowQuality</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC5pauseyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/pause()"></a>
<a class="token" href="#/s:7heresdk7MapViewC5pauseyyF">pause()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pauses rendering of this instance of map view.</p>
<p>Normally the application doesn’t need to call this method since the required handling of foreground/background switch is done
from inside the HERESDK. However, if this needs to be called for some special reasons on application side, the application
must call this method in<code>applicationWillResignActive(_:)</code> of the application delegate or
<code>sceneWillResignActive(_:)</code> of the scene delegate. Otherwise, it  may result in rendering glitches as the renderer is
prohibited from issuing rendering commands when being in background.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">pause</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC6resumeyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resume()"></a>
<a class="token" href="#/s:7heresdk7MapViewC6resumeyyF">resume()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resumes  rendering of this instance of map view.</p>
<p>Normally the application doesn’t need to call this method since the required handling of foreground/background switch is done
from inside the HERESDK. However, if this needs to be called for some special reasons on application side, the application
must call this method in <code>applicationDidBecomeActive(_:)</code> of the application delegate
or <code>sceneDidBecomeActive(_:)</code> of the scene delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">resume</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)HereMapView(im)init"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)HereMapView(im)init">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)HereMapView(im)initWithFrame:"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(frame:)"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)HereMapView(im)initWithFrame:">init(frame:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="k">override</span> <span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="nv">frame</span><span class="p">:</span> <span class="kt">CGRect</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC7optionsAcA0bC7OptionsV_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(options:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC7optionsAcA0bC7OptionsV_tcfc">init(options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes and returns a newly allocated view object</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapviewoptions">MapViewOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Customization of view for example its map projection</p>
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
<a name="/s:7heresdk7MapViewC5frame7optionsACSo6CGRectV_AA0bC7OptionsVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(frame:options:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC5frame7optionsACSo6CGRectV_AA0bC7OptionsVtcfc">init(frame:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes and returns a newly allocated view object with the specified frame rectangle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="nv">frame</span><span class="p">:</span> <span class="kt">CGRect</span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapviewoptions">MapViewOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>frame</em>
</code>
</td>
<td>
<div>
<p>The frame rectangle for the view, measured in points.</p>
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
<p>Customization of view for example its map projection</p>
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
<a name="/s:7heresdk7MapViewC5frame13withSdkEngine7optionsACSo6CGRectV_AA09SDKNativeG0CAA0bC7OptionsVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(frame:withSdkEngine:options:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC5frame13withSdkEngine7optionsACSo6CGRectV_AA09SDKNativeG0CAA0bC7OptionsVtcfc">init(frame:<wbr/>withSdkEngine:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes and returns a newly allocated view object with the specified frame rectangle and sdk engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="nv">frame</span><span class="p">:</span> <span class="kt">CGRect</span><span class="p">,</span> <span class="n">withSdkEngine</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapviewoptions">MapViewOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>frame</em>
</code>
</td>
<td>
<div>
<p>The frame rectangle for the view, measured in points.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>withSdkEngine</em>
</code>
</td>
<td>
<div>
<p>object used previously to initialize whole sdk</p>
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
<p>Optional customization of view for example its map projection</p>
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
<a name="/s:7heresdk7MapViewC5frame13withSdkEngineACSo6CGRectV_AA09SDKNativeG0Ctcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(frame:withSdkEngine:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC5frame13withSdkEngineACSo6CGRectV_AA09SDKNativeG0Ctcfc">init(frame:<wbr/>withSdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="nv">frame</span><span class="p">:</span> <span class="kt">CGRect</span><span class="p">,</span> <span class="n">withSdkEngine</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC5frame13withSdkEngine0E7OptionsACSo6CGRectV_AA09SDKNativeG0CAA0bcH0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(frame:withSdkEngine:withOptions:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC5frame13withSdkEngine0E7OptionsACSo6CGRectV_AA09SDKNativeG0CAA0bcH0VSgtcfc">init(frame:<wbr/>withSdkEngine:<wbr/>withOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes and returns a newly allocated view object with specified frame rectangle, sdk engine and options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">frame</span><span class="p">:</span> <span class="kt">CGRect</span><span class="p">,</span> <span class="n">withSdkEngine</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="n">withOptions</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapviewoptions">MapViewOptions</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>frame</em>
</code>
</td>
<td>
<div>
<p>The frame rectangle for the view, measured in points.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>withSdkEngine</em>
</code>
</td>
<td>
<div>
<p>Object that was previously used to initialize whole sdk.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>withOptions</em>
</code>
</td>
<td>
<div>
<p>Optional customization of view for example its map projection.</p>
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
<a name="/c:@M@heresdk@objc(cs)HereMapView(im)initWithCoder:"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coder:)"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)HereMapView(im)initWithCoder:">init(coder:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">required</span> <span class="nf">init</span><span class="p">?(</span><span class="n">coder</span> <span class="nv">aDecoder</span><span class="p">:</span> <span class="kt">NSCoder</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC7isValidSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isValid"></a>
<a class="token" href="#/s:7heresdk7MapViewC7isValidSbvp">isValid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether this instance is valid. It will be made invalid
when the corresponding <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> is destroyed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">isValid</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC05geoToC11Coordinates0dF0AA7Point2DVSgAA03GeoF0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/geoToViewCoordinates(geoCoordinates:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC05geoToC11Coordinates0dF0AA7Point2DVSgAA03GeoF0V_tF">geoToViewCoordinates(geoCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Converts geographical coordinates to view coordinates (in pixels).</p>
<p>If specified, altitude of the input coordinates is interpreted as altitude above sea level.
If not specified, the input coordinates are interpreted as being on ground elevation.
The above distinction is only relevant when 3D terrain feature is enabled.</p>
<p>The resulting view coordinates might be outside of current viewport, i.e. result might contain values
less than zero or greater than view’s dimensions.</p>
<p>If the render surface is not attached, it will return <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">geoToViewCoordinates</span><span class="p">(</span><span class="nv">geoCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoCoordinates</em>
</code>
</td>
<td>
<div>
<p>Geographical coordinates to convert.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The view coordinates of the specified geographical point or <code>nil</code>
if there is no render surface attached.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC20viewToGeoCoordinates0dG0AA0fG0VSgAA7Point2DV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/viewToGeoCoordinates(viewCoordinates:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC20viewToGeoCoordinates0dG0AA0fG0VSgAA7Point2DV_tF">viewToGeoCoordinates(viewCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Converts view coordinates to geographical coordinates.</p>
<p>An optional altitude component of the resulting geographical coordinate is not set.</p>
<p>If the view coordinates specify a point above a horizon, then the result
is geographical coordinates of the point on a horizon below the specified
view coordinates.</p>
<p>The fog effect is ignored for the calculation, meaning that for the view point
within the area covered by the fog, the result is geographical coordinates
that would be displayed at the specified point if the fog effect was
not applied.</p>
<p>If the render surface is not attached, it will return <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">viewToGeoCoordinates</span><span class="p">(</span><span class="nv">viewCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>viewCoordinates</em>
</code>
</td>
<td>
<div>
<p>Point inside the view to convert.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The geographical coordinates under specified view point or <code>nil</code> if there is no render surface attached.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bI6ResultCSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/pick(filter:inside:completion:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bI6ResultCSgctF">pick(filter:<wbr/>inside:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns all map content located inside the specified pick area. Content to be picked is
specified by a pick content filter.
The pick area is defined by a rectangle in map view coordinates
in pixels, relative to the map view’s origin at (0, 0) which indicates the top-left corner
of the map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">pick</span><span class="p">(</span><span class="nv">filter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapscene">MapScene</a></span><span class="o">.</span><span class="kt">MapPickFilter</span><span class="p">?,</span> <span class="n">inside</span> <span class="nv">viewArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">,</span> <span class="n">completion</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="p">(</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappickresult">MapPickResult</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>filter</em>
</code>
</td>
<td>
<div>
<p>Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewArea</em>
</code>
</td>
<td>
<div>
<p>The rectangular pixel area of the view inside which map content will be picked.
      View area is relative to the map view’s origin at (0, 0) at the top-left corner of the map view.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>Callback to call with the result. This will be called on a main thread when pick operation completes.</p>
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
<a name="/s:7heresdk7MapViewC14takeScreenshot8callbackyySo7UIImageCSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/takeScreenshot(callback:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC14takeScreenshot8callbackyySo7UIImageCSgc_tF">takeScreenshot(callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously retrieves a screenshot of current map view.
Note that this does not work when the map view is currently not visible, for example,
when an application is running in background - even if MapView.pause() was not called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">takeScreenshot</span><span class="p">(</span><span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Classes/MapView.html#/s:7heresdk7MapViewC22TakeScreenshotCallbacka">TakeScreenshotCallback</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>Completion handler called when the screenshot is completed.</p>
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
<a name="/s:7heresdk7MapViewC20addLifecycleDelegateyyAA0bceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC20addLifecycleDelegateyyAA0bceF0_pF">addLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></code> to this map view.
Adding the same object multiple times has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">addLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">lifecycleListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lifecycleListener</em>
</code>
</td>
<td>
<div>
<p>An object to be notified of lifecycle events.</p>
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
<a name="/s:7heresdk7MapViewC23removeLifecycleDelegateyyAA0bceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC23removeLifecycleDelegateyyAA0bceF0_pF">removeLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></code> from this map view.
Trying to remove an object that was not added or was removed before
has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">lifecycleListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lifecycleListener</em>
</code>
</td>
<td>
<div>
<p>An object to stop being notified of lifecycle events.</p>
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
<a name="/s:7heresdk7MapViewC6reinityyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/reinit()"></a>
<a class="token" href="#/s:7heresdk7MapViewC6reinityyF">reinit()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reinitializes the map renderer. Does nothing if <code><a href="../Classes/MapView.html#/s:7heresdk7MapViewC7isValidSbvp">isValid</a></code> is <code>true</code> or
<code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ">SDKNativeEngine.sharedInstance</a></code> is <code>nil</code>.</p>
<p>This can be used after <code>MapView</code> gets invalidated as a result of destroying the shared
<code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> and setting a new shared <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
<p>After this call finishes successfully, <code><a href="../Classes/MapView.html#/s:7heresdk7MapViewC7isValidSbvp">isValid</a></code> becomes <code>true</code>.</p>
<p>Map state is not preserved. The caller must load a scene, set camera, re-add all the delegates and all
the map items, etc.</p>
<p>Any previously stored instances of <code><a href="../Classes/MapView.html#/s:7heresdk7MapViewC6cameraAA0B6CameraCvp">MapView.camera</a></code>, <code><a href="../Classes/MapView.html#/s:7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp">MapView.mapScene</a></code>, <code><a href="../Classes/MapView.html#/s:7heresdk11MapViewBaseP10mapContextAA0bF0Cvp">MapView.mapContext</a></code>,
<code><a href="../Classes/MapView.html#/s:7heresdk7MapViewC8gesturesAA8GesturesCvp">MapView.gestures</a></code> and <code><a href="../Classes/MapView.html#/s:7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp">MapView.hereMap</a></code> remain invalid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">reinit</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWatermarkLocation(anchor:offset:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF">setWatermarkLocation(anchor:<wbr/>offset:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the position of the HERE logo watermark within the map view.</p>
<p>By default, the watermark is aligned to the bottom-right corner of the view:
Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
It is recommended to change the default position only if necessary to avoid overlapping UI elements.
The watermark should always be fully visible within the view.
The anchor point on the watermark is its center (width/2, height/2), around which it will be placed
in the map view.
For map views smaller than 250 dip in both width and height, the watermark will not be shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">setWatermarkLocation</span><span class="p">(</span><span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span><span class="p">,</span> <span class="nv">offset</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>anchor</em>
</code>
</td>
<td>
<div>
<p>Anchor point in normalized view coordinates [0, 1]. Map view’s origin at (0, 0) indicates
a top-left corner of the map view.
Out of boundary anchor point values will be clamped to the [0, 1] range.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>offset</em>
</code>
</td>
<td>
<div>
<p>A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that
allows shifting the watermark from the anchor point position in one or the other
direction.
For the quadrant of values expressing visible part of the map view negative offset shifts
the watermark to the direction of the origin, positive - away from it.
For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
the bottom.
If specified offset will result in watermark being completely or partially out-of-view
the offset will be adjusted internally so that watermark is fully visible.
Offset is not being scaled when the map view size changes.</p>
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
<a name="/s:7heresdk7MapViewC10pixelScaleSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pixelScale"></a>
<a class="token" href="#/s:7heresdk7MapViewC10pixelScaleSdvp">pixelScale</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The pixel scale factor used by this MapView.
It is used to support screen resolution and size independence.
This value is a derivative of the device’s screen pixel density and is a
direct analog of the native scale factor for the physical screen.</p>
<p>It can be used to translate between physical pixels and
points according to formula:
points = pixels / pixel_scale.</p>
<p>Pixel scale is 0.0 if the map view is not initialized.</p>
<p>In cases where the MapView moves in between screens (e.g. from main screen to a CarPlay screen),
the most up-to-date pixel scale value can be obtained after a render target gets attached to the view.
To get notified when a render target gets attached to the MapView, see <code>MapViewLifecycleDelegate.onAttach</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">pixelScale</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC13watermarkSizeAA6Size2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/watermarkSize"></a>
<a class="token" href="#/s:7heresdk7MapViewC13watermarkSizeAA6Size2DVvp">watermarkSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the size of the watermark in physical pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">watermarkSize</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-size2d">Size2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC03pinC0_2toAC0C3PinCSgSo6UIViewC_AA14GeoCoordinatesVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/pinView(_:to:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC03pinC0_2toAC0C3PinCSgSo6UIViewC_AA14GeoCoordinatesVtF">pinView(_:<wbr/>to:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pins a <code>UIView</code> to the <code>MapView</code> and returns a proxy object that can be used to
control the pinning. Trying to pin a view that was already pinned or a view
that has a super view has no effect and returns <code>nil</code>.</p>
<p>The altitude component of the coordinates, if set, is interpreted as above sea level.
When not set, the coordinates are interpreted as at ground level.</p>
<p>Please note, a pinned <code>UIView</code> will be confined to the bounds of <code>MapView</code> by default.
If this is not desired, setting <code>MapView</code>‘s property <code>clipsToBounds</code> to false will allow
pinned views to exceed <code>MapView</code>’s bounds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">pinView</span><span class="p">(</span><span class="n">_</span> <span class="nv">view</span><span class="p">:</span> <span class="kt">UIView</span><span class="p">,</span> <span class="n">to</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapview-viewpin">ViewPin</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>view</em>
</code>
</td>
<td>
<div>
<p><code>UIView</code> object to pin.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p><code><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></code> to pin the view at.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapview-viewpin">ViewPin</a></code> proxy object, or <code>nil</code> if view was not pinned.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC05unpinC0yySo6UIViewCF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/unpinView(_:)"></a>
<a class="token" href="#/s:7heresdk7MapViewC05unpinC0yySo6UIViewCF">unpinView(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a ViewPin from the MapView by specifying the corresponding UIView.
Trying to unpin a view that was not pinned or was unpinned before has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">unpinView</span><span class="p">(</span><span class="n">_</span> <span class="nv">view</span><span class="p">:</span> <span class="kt">UIView</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>view</em>
</code>
</td>
<td>
<div>
<p>The UIView corresponding to the ViewPin to remove.</p>
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
<a name="/s:7heresdk7MapViewC8viewPinsSayAC0C3PinCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewPins"></a>
<a class="token" href="#/s:7heresdk7MapViewC8viewPinsSayAC0C3PinCGvp">viewPins</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a copy of the array of currently added view pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">viewPins</span><span class="p">:</span> <span class="p">[</span><span class="kt">MapView</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapview-viewpin">ViewPin</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7MapViewC15handleLowMemoryyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/handleLowMemory()"></a>
<a class="token" href="#/s:7heresdk7MapViewC15handleLowMemoryyyF">handleLowMemory()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Handles low memory situation.</p>
<p>This method should be called from a view controller, when it receives
a memory warning (<code>UIViewController.didReceiveMemoryWarning()</code>)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@MainActor</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">handleLowMemory</span><span class="p">()</span></code></pre>
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
