---
title: "TransitDeparture Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-transitdeparture"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TransitDeparture.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitDeparture"></a>
<a title="TransitDeparture Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TransitDeparture Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct TransitDeparture : Hashable</code></pre>
</div>
</div>
<p>This struct holds the transit departure or arrival information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/place"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp">place</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The departure or arrival place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var place: RoutePlace</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV4time10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/time"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV4time10Foundation4DateVSgvp">time</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Expected departure or arrival time of the event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var time: Date?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5delays5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/delay"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5delays5Int32VSgvp">delay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The accumulated delay in seconds from the scheduled time of the event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var delay: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/status"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp">status</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Status of the departure.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var status: TransitDepartureStatus?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(place:time:delay:status:)"></a>
<a class="token" href="#/s:7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc">init(place:<wbr/>time:<wbr/>delay:<wbr/>status:<wbr/>)</a>
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
<pre><code>public init(place: RoutePlace, time: Date? = nil, delay: Int32? = nil, status: TransitDepartureStatus? = nil)</code></pre>
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



</div>
`
}</HTMLBlock>
