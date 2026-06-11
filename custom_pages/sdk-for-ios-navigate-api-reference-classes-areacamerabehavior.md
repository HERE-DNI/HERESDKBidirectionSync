---
title: "AreaCameraBehavior"
slug: "sdk-for-ios-navigate-api-reference-classes-areacamerabehavior"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/AreaCameraBehavior"></a>
<a title="AreaCameraBehavior Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        AreaCameraBehavior Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AreaCameraBehavior</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AreaCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AreaCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AreaCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to show an overview of geo points. By default, the orientation of the camera will be
perpendicular to the Earth’s surface (ie. looking towards the center of the Earth),
while bearing will be towards north.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/normalizedPrincipalPoint"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp">normalizedPrincipalPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">normalizedPrincipalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewRectangle"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp">viewRectangle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates.
Defaults to <code>nil</code>. If not set, it uses the viewport bounds of the underlying map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC23cameraAnimationDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraAnimationDuration"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC23cameraAnimationDurationSdvp">cameraAnimationDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration of camera animation in milliseconds.
If there is an animation, it will last for specified period of time.
Defaults to 500 milliseconds, or half a second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraAnimationDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC31principalPointAnimationDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/principalPointAnimationDuration"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC31principalPointAnimationDurationSdvp">principalPointAnimationDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration of principal point animation in milliseconds.
If the principal point is changed, the change will be animated
over this duration.
Defaults to 500 milliseconds, or half a second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">principalPointAnimationDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC7maxZoomAA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxZoom"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC7maxZoomAA10MapMeasureVvp">maxZoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximal allowed zoom.
Defines maximal zoom level to be applied to enclose geodetic bounding box.
Defaults to a <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></code> with kind <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> and value 20.0.
Note: <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO5scaleyA2EmF">MapMeasure.Kind.scale</a></code> is not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC22cameraBearingInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraBearingInDegrees"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC22cameraBearingInDegreesSdvp">cameraBearingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera bearing in degrees.
The direction in which the camera will point in degrees clockwise, relative to
true North. The input should range between [0, 360]. Defaults to true North (0 degrees).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraBearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC19cameraTiltInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraTiltInDegrees"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC19cameraTiltInDegreesSdvp">cameraTiltInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera tilt in degrees.
The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
0 degrees, meaning that it will look straight down into the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraTiltInDegrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC25isCurrentPositionIncludedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCurrentPositionIncluded"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC25isCurrentPositionIncludedSbvp">isCurrentPositionIncluded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Include current position in camera view.
Decides if the current position should be added to the set of visible points.
Note that if the current position is in the vicinity of any of the visible points, setting this to
<code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
or it will try to include the current position. Defaults to false.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCurrentPositionIncluded</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC16setVisiblePoints07visibleG0ySayAA14GeoCoordinatesVG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setVisiblePoints(visiblePoints:)"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC16setVisiblePoints07visibleG0ySayAA14GeoCoordinatesVG_tF">setVisiblePoints(visiblePoints:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the list of geo points to show in the camera view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setVisiblePoints</span><span class="p">(</span><span class="nv">visiblePoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>visiblePoints</em>
</code>
</td>
<td>
<div>
<p>The list of geo points to visualize. The list can be empty.</p>
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
<a name="/s:7heresdk18AreaCameraBehaviorC16getVisiblePointsSayAA14GeoCoordinatesVGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVisiblePoints()"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC16getVisiblePointsSayAA14GeoCoordinatesVGyF">getVisiblePoints()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets configured visible geo points.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVisiblePoints</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The list of geo points to show in the camera view. The list can be empty.</p>
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
