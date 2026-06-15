---
title: "LaneDirectionCategory"
slug: "sdk-for-ios-navigate-api-reference-structs-lanedirectioncategory"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneDirectionCategory"></a>
<a title="LaneDirectionCategory Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        LaneDirectionCategory Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneDirectionCategory</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneDirectionCategory</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Indicates the directions of a lane. Most lanes lead only to one direction,
but there can be also lanes that split up into multiple directions.
A road can consist of multiple lanes towards the same direction.
Note: All members can be <code>true</code> or <code>false</code> at the same time. Lanes such as bicycle
lanes mostly never contain a direction category and thus, all members are <code>false</code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV8straightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/straight"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV8straightSbvp">straight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes straight up.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">straight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV12slightlyLeftSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/slightlyLeft"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV12slightlyLeftSbvp">slightlyLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes slightly left.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">slightlyLeft</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV9quiteLeftSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/quiteLeft"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV9quiteLeftSbvp">quiteLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes quite left.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">quiteLeft</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV8hardLeftSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hardLeft"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV8hardLeftSbvp">hardLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes hard left.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hardLeft</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV9uTurnLeftSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/uTurnLeft"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV9uTurnLeftSbvp">uTurnLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that makes a left u-turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">uTurnLeft</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV13slightlyRightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/slightlyRight"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV13slightlyRightSbvp">slightlyRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes slightly right.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">slightlyRight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV10quiteRightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/quiteRight"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV10quiteRightSbvp">quiteRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes quite right.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">quiteRight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV9hardRightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hardRight"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV9hardRightSbvp">hardRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that goes hard right.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hardRight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV10uTurnRightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/uTurnRight"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV10uTurnRightSbvp">uTurnRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane that makes a right u-turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">uTurnRight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV8straight12slightlyLeft05quiteG004hardG005uTurnG00F5Right0hK00iK001ujK0ACSb_S8btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(straight:slightlyLeft:quiteLeft:hardLeft:uTurnLeft:slightlyRight:quiteRight:hardRight:uTurnRight:)"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV8straight12slightlyLeft05quiteG004hardG005uTurnG00F5Right0hK00iK001ujK0ACSb_S8btcfc">init(straight:<wbr/>slightlyLeft:<wbr/>quiteLeft:<wbr/>hardLeft:<wbr/>uTurnLeft:<wbr/>slightlyRight:<wbr/>quiteRight:<wbr/>hardRight:<wbr/>uTurnRight:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">straight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">slightlyLeft</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">quiteLeft</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">hardLeft</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">uTurnLeft</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">slightlyRight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">quiteRight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">hardRight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">uTurnRight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
