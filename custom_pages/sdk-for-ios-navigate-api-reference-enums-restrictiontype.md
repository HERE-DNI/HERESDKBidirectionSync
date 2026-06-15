---
title: "RestrictionType"
slug: "sdk-for-ios-navigate-api-reference-enums-restrictiontype"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RestrictionType"></a>
<a title="RestrictionType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-transport">Transport</a>

        RestrictionType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RestrictionType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RestrictionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Type of vehicle restriction.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO6weightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/weight"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO6weightyA2CmF">weight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Actual weight, in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">weight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO11grossWeightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/grossWeight"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO11grossWeightyA2CmF">grossWeight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gross vehicle mass, in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">grossWeight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO13weightPerAxleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/weightPerAxle"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO13weightPerAxleyA2CmF">weightPerAxle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weight per axle, in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">weightPerAxle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO15payloadCapacityyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/payloadCapacity"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO15payloadCapacityyA2CmF">payloadCapacity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payload capacity weight, in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">payloadCapacity</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO11emptyWeightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emptyWeight"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO11emptyWeightyA2CmF">emptyWeight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Empty vehicle weight (tare weight), in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">emptyWeight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO6heightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/height"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO6heightyA2CmF">height</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A height, in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">height</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO5widthyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/width"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO5widthyA2CmF">width</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A width, in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">width</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO6lengthyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/length"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO6lengthyA2CmF">length</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A length, in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">length</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO38kingpinToRearAxleDistanceInCentimetersyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/kingpinToRearAxleDistanceInCentimeters"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO38kingpinToRearAxleDistanceInCentimetersyA2CmF">kingpinToRearAxleDistanceInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance from kingpin to rear axle, in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">kingpinToRearAxleDistanceInCentimeters</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO13wheelsPerAxleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/wheelsPerAxle"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO13wheelsPerAxleyA2CmF">wheelsPerAxle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Wheels per axle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">wheelsPerAxle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO20distanceBetweenAxlesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/distanceBetweenAxles"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO20distanceBetweenAxlesyA2CmF">distanceBetweenAxles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance between axles, in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">distanceBetweenAxles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO18weightPerAxleCountyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/weightPerAxleCount"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO18weightPerAxleCountyA2CmF">weightPerAxleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weight per number of axles, in kilograms. See <code><a href="../Structs/VehicleRestriction.html#/s:7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp">VehicleRestriction.axleCount</a></code>
for information on number of axles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">weightPerAxleCount</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO18weightPerAxleGroupyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/weightPerAxleGroup"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO18weightPerAxleGroupyA2CmF">weightPerAxleGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weight per axle group, in kilograms. See <code><a href="../Structs/VehicleRestriction.html#/s:7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp">VehicleRestriction.axleCountInGroup</a></code>
for information about axle group.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">weightPerAxleGroup</span></code></pre>
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
