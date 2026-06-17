---
title: "ParkingType"
slug: "sdk-for-ios-explore-enums-parkingtype"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ParkingType"></a>
<a title="ParkingType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-search">Search</a>

        ParkingType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ParkingType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ParkingType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents parking type available at the location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO13alongMotorwayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/alongMotorway"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO13alongMotorwayyA2CmF">alongMotorway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A parking facility/rest area along a motorway, freeway, interstate, highway etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">alongMotorway</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO13parkingGarageyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parkingGarage"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO13parkingGarageyA2CmF">parkingGarage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Multi-story car park, mainly above ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">parkingGarage</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO10parkingLotyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parkingLot"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO10parkingLotyA2CmF">parkingLot</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A cleared area that is intended for parking vehicles, i.e. at super markets, bars, etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">parkingLot</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO10onDrivewayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onDriveway"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO10onDrivewayyA2CmF">onDriveway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The driveway of a house or building.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">onDriveway</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO8onStreetyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onStreet"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO8onStreetyA2CmF">onStreet</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A public parking space along a street.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">onStreet</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ParkingTypeO17undergroundGarageyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/undergroundGarage"></a>
<a class="token" href="#/s:7heresdk11ParkingTypeO17undergroundGarageyA2CmF">undergroundGarage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Multi-story car park, mainly underground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">undergroundGarage</span></code></pre>
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
