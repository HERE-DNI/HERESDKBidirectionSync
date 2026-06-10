---
title: "sdk-for-ios-explore-api-reference-structs-localizedroadnumber"
slug: "sdk-for-ios-explore-api-reference-structs-localizedroadnumber"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedRoadNumber"></a>
<a title="LocalizedRoadNumber Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocalizedRoadNumber Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocalizedRoadNumber</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocalizedRoadNumber</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Used to represent road number localized to specific language with optional direction and route type information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV09localizedD0AA0B4TextVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localizedNumber"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV09localizedD0AA0B4TextVvp">localizedNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road number with locale information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localizedNumber</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-localizedtext">LocalizedText</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV9directionAA17CardinalDirectionOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/direction"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV9directionAA17CardinalDirectionOSgvp">direction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road direction.
This property indicates the official directional identifier assigned to highways.
Can be <code>nil</code> when direction is not assigned to highways.
The direction indicates the same information as on the signpost shield: For example, if is “101 West”, the directions contains WEST.
Note that the official direction is not necessarily the travel direction.
For example, US-101 through the city of Sunnyvale is physically located East to West.
However, the official direction on sign is North/South.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">direction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-cardinaldirection">CardinalDirection</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV9routeTypeAA05RouteF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeType"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV9routeTypeAA05RouteF0Ovp">routeType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route type of the LocalizedRoadNumber.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-routetype">RouteType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV09localizedD09direction9routeTypeAcA0B4TextV_AA17CardinalDirectionOSgAA05RouteH0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(localizedNumber:direction:routeType:)"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV09localizedD09direction9routeTypeAcA0B4TextV_AA17CardinalDirectionOSgAA05RouteH0Otcfc">init(localizedNumber:<wbr/>direction:<wbr/>routeType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">localizedNumber</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-localizedtext">LocalizedText</a></span><span class="p">,</span> <span class="nv">direction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-cardinaldirection">CardinalDirection</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">routeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-routetype">RouteType</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV08completecD0SSyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/completeRoadNumber()"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV08completecD0SSyF">completeRoadNumber()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the whole road number information including its cardinal direction.
In case direction is empty, the original localized text will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">completeRoadNumber</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">String</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The whole road number information including its cardinal direction.</p>
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
