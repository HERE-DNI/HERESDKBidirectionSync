---
title: "CarSpecifications"
slug: "sdk-for-ios-explore-api-reference-structs-carspecifications"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CarSpecifications"></a>
<a title="CarSpecifications Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-transport">Transport</a>

        CarSpecifications Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CarSpecifications</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use TransportSpecification instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CarSpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV22grossWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/grossWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV22grossWeightInKilogramss5Int32VSgvp">grossWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car weight including trailers and shipped goods in kilograms. The provided value
must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong>
This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV19heightInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/heightInCentimeters"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV19heightInCentimeterss5Int32VSgvp">heightInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV18widthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/widthInCentimeters"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV18widthInCentimeterss5Int32VSgvp">widthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV19lengthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInCentimeters"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV19lengthInCentimeterss5Int32VSgvp">lengthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
When specifying <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">CarSpecifications.trailerAxleCount</a></code>, then <code>CarSpecifications.axleCount</code> is required and must be greater than <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">CarSpecifications.trailerAxleCount</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 1]. By default, it is not set.
When specifying <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">CarSpecifications.trailerAxleCount</a></code>, then <code>CarSpecifications.trailerCount</code> is required and must be greater than 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerAxleCount"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">trailerAxleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">CarSpecifications.axleCount</a></code>, hence <code>CarSpecifications.trailerAxleCount</code> must be less than <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">CarSpecifications.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">CarSpecifications.axleCount</a></code> and <code><a href="../Structs/CarSpecifications.html#/s:7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp">CarSpecifications.trailerCount</a></code> are required to specify <code>CarSpecifications.trailerAxleCount</code>.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI09axleCount07trailerM00n4AxleM0ACs5Int32VSg_A6Mtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(grossWeightInKilograms:heightInCentimeters:widthInCentimeters:lengthInCentimeters:axleCount:trailerCount:trailerAxleCount:)"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI09axleCount07trailerM00n4AxleM0ACs5Int32VSg_A6Mtcfc">init(grossWeightInKilograms:<wbr/>heightInCentimeters:<wbr/>widthInCentimeters:<wbr/>lengthInCentimeters:<wbr/>axleCount:<wbr/>trailerCount:<wbr/>trailerAxleCount:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
