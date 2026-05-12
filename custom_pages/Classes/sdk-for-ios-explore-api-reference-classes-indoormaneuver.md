---
title: "IndoorManeuver Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-indoormaneuver"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- IndoorManeuver.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/IndoorManeuver"></a>
<a title="IndoorManeuver Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IndoorManeuver Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class IndoorManeuver</code></pre>
<pre><code>extension IndoorManeuver: NativeBase</code></pre>
<pre><code>extension IndoorManeuver: Hashable</code></pre>
</div>
</div>
<p>Represents a maneuver within an indoor section.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC6actionAA0bC7ActionsOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/action"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC6actionAA0bC7ActionsOSgvp">action</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The action type of this maneuver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var action: IndoorManeuverActions? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC10coordinateAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinate"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC10coordinateAA14GeoCoordinatesVvp">coordinate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of this maneuver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var coordinate: GeoCoordinates { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC6offsets5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offset"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC6offsets5Int32Vvp">offset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The offset of this maneuver from the start of the section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var offset: Int32 { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC12sectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionIndex"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC12sectionIndexs5Int32Vvp">sectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The section index this maneuver belongs to.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var sectionIndex: Int32 { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC14lengthInMetersSfvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC14lengthInMetersSfvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of this maneuver in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var lengthInMeters: Float { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration to complete this maneuver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var duration: TimeInterval { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC11levelZIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levelZIndex"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC11levelZIndexs5Int32Vvp">levelZIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vertical level index of this maneuver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var levelZIndex: Int32 { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC15indoorSpaceDataAA0beF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorSpaceData"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC15indoorSpaceDataAA0beF0VSgvp">indoorSpaceData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var indoorSpaceData: IndoorSpaceData? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IndoorManeuverC21indoorLevelChangeDataAA0befG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorLevelChangeData"></a>
<a class="token" href="#/s:7heresdk14IndoorManeuverC21indoorLevelChangeDataAA0befG0VSgvp">indoorLevelChangeData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var indoorLevelChangeData: IndoorLevelChangeData? { get }</code></pre>
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
