---
title: "Maneuver Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-maneuver"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Maneuver.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/Maneuver"></a>
<a title="Maneuver Class Reference"></a>
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
        Maneuver Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class Maneuver</code></pre>
<pre><code>extension Maneuver: NativeBase</code></pre>
<pre><code>extension Maneuver: Hashable</code></pre>
</div>
</div>
<p>This class provides all the information for a maneuver. The directional information (e.g. road names, road
numbers and signpost direction) is stored in <code><a href="../Classes/Maneuver.html#/s:7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp">Maneuver.roadTexts</a></code> and <code><a href="../Classes/Maneuver.html#/s:7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp">Maneuver.nextRoadTexts</a></code> attributes.
As for the motorway exit information, it can be obtained from <code><a href="../Classes/Maneuver.html#/s:7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp">Maneuver.exitSignTexts</a></code> attribute.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC6actionAA0B6ActionOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/action"></a>
<a class="token" href="#/s:7heresdk8ManeuverC6actionAA0B6ActionOvp">action</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the maneuver action.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var action: ManeuverAction { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk8ManeuverC11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic coordinates where the maneuver is located.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var coordinates: GeoCoordinates { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC6offsets5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offset"></a>
<a class="token" href="#/s:7heresdk8ManeuverC6offsets5Int32Vvp">offset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index over <code><a href="../Classes/Section.html#/s:7heresdk7SectionC8geometryAA11GeoPolylineVvp">Section.geometry</a></code> where the maneuver is located.</p>
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
<a name="/s:7heresdk8ManeuverC11countryCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk8ManeuverC11countryCodeSSSgvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The country code of the maneuver position. The value is <code>nil</code> when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var countryCode: String? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/exitSignTexts"></a>
<a class="token" href="#/s:7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp">exitSignTexts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var exitSignTexts: LocalizedTexts { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk8ManeuverC14lengthInMeterss5Int32Vvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of the maneuver in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var lengthInMeters: Int32 { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadTexts"></a>
<a class="token" href="#/s:7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp">roadTexts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
<strong>Note:</strong> These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var roadTexts: RoadTexts { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/nextRoadTexts"></a>
<a class="token" href="#/s:7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp">nextRoadTexts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var nextRoadTexts: RoadTexts { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC8signpostAA8SignpostVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/signpost"></a>
<a class="token" href="#/s:7heresdk8ManeuverC8signpostAA8SignpostVSgvp">signpost</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the <code><a href="sdk-for-ios-explore-api-reference-..-structs-signpost">Signpost</a></code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var signpost: Signpost? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC17intersectionNamesAA14LocalizedTextsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/intersectionNames"></a>
<a class="token" href="#/s:7heresdk8ManeuverC17intersectionNamesAA14LocalizedTextsVvp">intersectionNames</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The textual attributes of the intersection.
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
<strong>Note:</strong> Routes calculated with OfflineRoutingEngine are not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var intersectionNames: LocalizedTexts { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC4textSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/text"></a>
<a class="token" href="#/s:7heresdk8ManeuverC4textSSvp">text</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maneuver instruction. The text is formatted and localized as specified via
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routetextoptions">RouteTextOptions</a></code>.
<strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code>EventTextListener</code> texts are meant to be used
for spoken voice announcements during a trip.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var text: String { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC12sectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionIndex"></a>
<a class="token" href="#/s:7heresdk8ManeuverC12sectionIndexs5Int32Vvp">sectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index over <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code> indicating the section to which the maneuver belongs to.</p>
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
<a name="/s:7heresdk8ManeuverC9spanIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanIndex"></a>
<a class="token" href="#/s:7heresdk8ManeuverC9spanIndexs5Int32Vvp">spanIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index over <code><a href="../Classes/Section.html#/s:7heresdk7SectionC5spansSayAA4SpanCGvp">Section.spans</a></code> indicating the first span after the maneuver point.
<strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
<code><a href="../Enums/ManeuverAction.html#/s:7heresdk14ManeuverActionO6arriveyA2CmF">ManeuverAction.arrive</a></code>) cannot be used, since these maneuvers are placed after the last span of the route and
the span index for them would be greater than the span list size.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var spanIndex: Int32 { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk8ManeuverC8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds needed to perform the maneuver.</p>
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
<a name="/s:7heresdk8ManeuverC18turnAngleInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/turnAngleInDegrees"></a>
<a class="token" href="#/s:7heresdk8ManeuverC18turnAngleInDegreesSdSgvp">turnAngleInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The angle of the turn component of the maneuver.
The angle increases clockwise and small values are used for going straight, i.e. a positive number
means there is a right turn and a negative number is a left turn.
Some maneuvers like Depart, Arrive and Roundabout pass doesn’t have a well defined angle, so the value
is omitted.
<strong>Note:</strong> These attributes are only available for the Navigate license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var turnAngleInDegrees: Double? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8ManeuverC24roundaboutAngleInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roundaboutAngleInDegrees"></a>
<a class="token" href="#/s:7heresdk8ManeuverC24roundaboutAngleInDegreesSdSgvp">roundaboutAngleInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route
parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from
the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a
vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects
the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive
in right-hand side driving country, and negative in left-hand side countries.
Note that the value is available for both the enter roundabout actions and the exit roundabout
actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the
roundabout itself is not representing a perfect circle, then the accuracy of the angle may be
compromised.
<strong>Note:</strong> These attributes are only available for the Navigate license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var roundaboutAngleInDegrees: Double? { get }</code></pre>
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
