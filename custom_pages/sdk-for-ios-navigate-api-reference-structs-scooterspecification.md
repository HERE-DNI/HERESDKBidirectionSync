---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-scooterspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ScooterSpecification.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScooterSpecification"></a>
<a title="ScooterSpecification Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-transport">Transport</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ScooterSpecification Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ScooterSpecification</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScooterSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Scooter specific settings.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20ScooterSpecificationV05allowB9OnHighwaySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowScooterOnHighway"></a>
<a class="token" href="#/s:7heresdk20ScooterSpecificationV05allowB9OnHighwaySbvp">allowScooterOnHighway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise.
Defaults to <code>false</code>.
Note that there is a similar parameter in <code><a href="sdk-for-ios-navigate-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code>, to disallow highway usage,
see <code>RoadFeatures.CONTROLLED_ACCESS_HIGHWAY</code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionnotice">SectionNotice</a></code> will be provided in the related <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> to indicate that
the highway usage restriction is violated on this route.
A few examples:</p>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
when no route is found without highway usage, a notice is received.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowScooterOnHighway</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20ScooterSpecificationV05allowB9OnHighwayACSb_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(allowScooterOnHighway:)"></a>
<a class="token" href="#/s:7heresdk20ScooterSpecificationV05allowB9OnHighwayACSb_tcfc">init(allowScooterOnHighway:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>allowScooterOnHighway: Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise.
Defaults to <code>false</code>.
Note that there is a similar parameter in <code><a href="sdk-for-ios-navigate-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code>, to disallow highway usage,
see <code>RoadFeatures.CONTROLLED_ACCESS_HIGHWAY</code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionnotice">SectionNotice</a></code> will be provided in the related <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> to indicate that
the highway usage restriction is violated on this route.
A few examples:</li>
</ul>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
  highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
  highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
  highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
  when no route is found without highway usage, a notice is received.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">allowScooterOnHighway</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

</div>
`
}</HTMLBlock>
