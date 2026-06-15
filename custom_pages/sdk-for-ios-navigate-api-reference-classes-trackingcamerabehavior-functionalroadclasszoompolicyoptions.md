---
title: "FunctionalRoadClassZoomPolicyOptions"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FunctionalRoadClassZoomPolicyOptions"></a>
<a title="FunctionalRoadClassZoomPolicyOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>

        FunctionalRoadClassZoomPolicyOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FunctionalRoadClassZoomPolicyOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FunctionalRoadClassZoomPolicyOptions</span></code></pre>
</div>
</div>
<p>Configuration for mapping functional road classes to zoom levels.
For correct default initialization, use <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/defaultZoom"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp">defaultZoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Default zoom returned when the functional road class is missing or unmapped.
Defaults to a <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></code> with kind <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> and value 16.5.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">defaultZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV010functionalfg2ToH0SDyAA0efG0OAA10MapMeasureVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/functionalRoadClassToZoom"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV010functionalfg2ToH0SDyAA0efG0OAA10MapMeasureVGvp">functionalRoadClassToZoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maps each functional road class to the zoom that should be used for it.
If <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)</a></code> is not used
for <code>TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</code>, it will be an empty map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">functionalRoadClassToZoom</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0010functionalfg2ToH0AeA10MapMeasureV_SDyAA0efG0OAIGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(defaultZoom:functionalRoadClassToZoom:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0010functionalfg2ToH0AeA10MapMeasureV_SDyAA0efG0OAIGtcfc">init(defaultZoom:<wbr/>functionalRoadClassToZoom:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n"><a href="../../Classes/TrackingCameraBehavior/FunctionalRoadClassZoomPolicyOptions.html#/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV07defaultH0AA10MapMeasureVvp">defaultZoom</a></span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="o">.</span><span class="n">zoomLevel</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="mf">16.5</span><span class="p">),</span> <span class="nv">functionalRoadClassToZoom</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[:])</span></code></pre>
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
} </HTMLBlock>
