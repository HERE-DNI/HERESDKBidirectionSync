---
title: "ManeuverRule"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverrule"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverRule"></a>
<a title="ManeuverRule Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>

        ManeuverRule Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverRule</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverRule</span></code></pre>
</div>
</div>
<p>Defines a single rule that determines how <code><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> reacts to nearby
maneuvers when the current position matches this rule.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClassesSayAA010FunctionalH5ClassOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/functionalRoadClasses"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClassesSayAA010FunctionalH5ClassOGvp">functionalRoadClasses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of functional road classes for which this rule applies. The list is unordered.
When empty, this rule applies to all functional road classes. Defaults to an empty list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">functionalRoadClasses</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV15maneuverActionsSayAA0E6ActionOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverActions"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV15maneuverActionsSayAA0E6ActionOGvp">maneuverActions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of maneuver actions for which this rule applies. The list is unordered.
When empty, this rule applies to all maneuver actions. Defaults to an empty list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverActions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuveraction">ManeuverAction</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV08maneuverF7OptionsAC0efH0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverRuleOptions"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV08maneuverF7OptionsAC0efH0VSgvp">maneuverRuleOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options for this rule. When set to <code>nil</code>, the camera does not
react to maneuvers that match this rule. Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverRuleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverruleoptions">ManeuverRuleOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClasses15maneuverActions0jF7OptionsAESayAA010FunctionalH5ClassOG_SayAA0E6ActionOGAC0efL0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(functionalRoadClasses:maneuverActions:maneuverRuleOptions:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClasses15maneuverActions0jF7OptionsAESayAA010FunctionalH5ClassOG_SayAA0E6ActionOGAC0efL0VSgtcfc">init(functionalRoadClasses:<wbr/>maneuverActions:<wbr/>maneuverRuleOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">functionalRoadClasses</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">maneuverActions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuveraction">ManeuverAction</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">maneuverRuleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverruleoptions">ManeuverRuleOptions</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
