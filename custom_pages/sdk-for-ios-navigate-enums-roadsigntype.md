---
title: "RoadSignType"
slug: "sdk-for-ios-navigate-enums-roadsigntype"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadSignType"></a>
<a title="RoadSignType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        RoadSignType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadSignType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadSignType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>A road sign type classifying road signs that can appear along a road.
Some signs are standardized and look the same in all countries, e.g. <code><a href="../Enums/RoadSignType.html#/s:7heresdk12RoadSignTypeO04stopC0yA2CmF">RoadSignType.stopSign</a></code>.
In general, the visual appearance of the road signs can differ across countries.
Some road signs can be combined with other signs, like <code><a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a></code> signs. The road sign will be always shown topmost.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unknown road sign type</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknown</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO19startOfNoOvertakingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/startOfNoOvertaking"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO19startOfNoOvertakingyA2CmF">startOfNoOvertaking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the starting of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#No_overtaking_or_passing_signs">Start of no overtaking sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">startOfNoOvertaking</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO17endOfNoOvertakingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOfNoOvertaking"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO17endOfNoOvertakingyA2CmF">endOfNoOvertaking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the ending of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#End_of_overtaking_signs">End of no overtaking sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOfNoOvertaking</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO28protectedOvertakingExtraLaneyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/protectedOvertakingExtraLane"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO28protectedOvertakingExtraLaneyA2CmF">protectedOvertakingExtraLane</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating an extra lane for overtaking. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-3.svg">Protected overtaking extra lane sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">protectedOvertakingExtraLane</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO37protectedOvertakingExtraLaneRightSideyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/protectedOvertakingExtraLaneRightSide"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO37protectedOvertakingExtraLaneRightSideyA2CmF">protectedOvertakingExtraLaneRightSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating an extra lane for overtaking on the right side. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-16.svg">Protected overtaking extra lane on the right side sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">protectedOvertakingExtraLaneRightSide</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO36protectedOvertakingExtraLaneLeftSideyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/protectedOvertakingExtraLaneLeftSide"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO36protectedOvertakingExtraLaneLeftSideyA2CmF">protectedOvertakingExtraLaneLeftSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating an extra lane for overtaking on the left side. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_R6-29.svg">Protected overtaking extra lane on the left side sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">protectedOvertakingExtraLaneLeftSide</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO14laneMergeRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/laneMergeRight"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO14laneMergeRightyA2CmF">laneMergeRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating merging of the right lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W4-3R.svg">Merge right lane sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">laneMergeRight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13laneMergeLeftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/laneMergeLeft"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13laneMergeLeftyA2CmF">laneMergeLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating merging of the left lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Mauritius#/media/File:Mauritius_Road_Signs_-_Warning_Sign_-_Traffic_Merging_From_Left_Behind.svg">Merge left lane sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">laneMergeLeft</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15laneMergeCenteryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/laneMergeCenter"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15laneMergeCenteryA2CmF">laneMergeCenter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating merging of the center lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:Roadsign_lane_drop_ahead.svg">Merge center lane sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">laneMergeCenter</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO24railwayCrossingProtectedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/railwayCrossingProtected"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO24railwayCrossingProtectedyA2CmF">railwayCrossingProtected</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a protected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-4.svg">Protected railway crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">railwayCrossingProtected</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO26railwayCrossingUnprotectedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/railwayCrossingUnprotected"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO26railwayCrossingUnprotectedyA2CmF">railwayCrossingUnprotected</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating an unprotected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-7-L.svg">Protected railway crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">railwayCrossingUnprotected</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO11roadNarrowsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/roadNarrows"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO11roadNarrowsyA2CmF">roadNarrows</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a narrowing road. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W4-3.svg">Road narrows sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">roadNarrows</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO14sharpCurveLeftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpCurveLeft"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO14sharpCurveLeftyA2CmF">sharpCurveLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a sharp curve to the left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512L.svg">Sharp curve left sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sharpCurveLeft</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15sharpCurveRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpCurveRight"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15sharpCurveRightyA2CmF">sharpCurveRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a sharp curve to the right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512.svg">Sharp curve right sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sharpCurveRight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO07windingB12StartingLeftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/windingRoadStartingLeft"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO07windingB12StartingLeftyA2CmF">windingRoadStartingLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a winding road starting left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513.svg">Winding road starting left sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">windingRoadStartingLeft</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO07windingB13StartingRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/windingRoadStartingRight"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO07windingB13StartingRightyA2CmF">windingRoadStartingRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a winding road starting right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513R.svg">Winding road starting right sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">windingRoadStartingRight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO25startOfNoOvertakingTrucksyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/startOfNoOvertakingTrucks"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO25startOfNoOvertakingTrucksyA2CmF">startOfNoOvertakingTrucks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no overtaking trucks. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4c.svg">No overtaking trucks sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">startOfNoOvertakingTrucks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO23endOfNoOvertakingTrucksyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOfNoOvertakingTrucks"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO23endOfNoOvertakingTrucksyA2CmF">endOfNoOvertakingTrucks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the end of no overtaking trucks zone. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4d.svg">End of no overtaking trucks sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOfNoOvertakingTrucks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO16steepHillUpwardsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/steepHillUpwards"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO16steepHillUpwardsyA2CmF">steepHillUpwards</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a steep hill upwards. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(b).svg">Steep hills upwards sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">steepHillUpwards</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO18steepHillDownwardsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/steepHillDownwards"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO18steepHillDownwardsyA2CmF">steepHillDownwards</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a steep hill downward. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(a).svg">Steep hills downwards sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">steepHillDownwards</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO04stopC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/stopSign"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO04stopC0yA2CmF">stopSign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a stop. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_RUS-027.svg">Stop sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">stopSign</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO11lateralWindyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/lateralWind"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO11lateralWindyA2CmF">lateralWind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating lateral winds. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-226.svg">Lateral winds sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">lateralWind</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO014generalWarningC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/generalWarningSign"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO014generalWarningC0yA2CmF">generalWarningSign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a general warning. Example: <a href="https://en.wikipedia.org/wiki/File:Hong_Kong_road_sign_240.svg">General warning sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">generalWarningSign</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15riskOfGroundingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/riskOfGrounding"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15riskOfGroundingyA2CmF">riskOfGrounding</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating risk of grounding. Example: <a href="https://en.wikipedia.org/wiki/File:Croatia_road_sign_A31.svg">Risk of grounding sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">riskOfGrounding</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO12generalCurveyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/generalCurve"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO12generalCurveyA2CmF">generalCurve</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a general curve. Example: <a href="https://en.wikipedia.org/wiki/File:Italian_traffic_signs_-_curva_pericolosa_a_sinistra.svg">General curve sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">generalCurve</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO20endOfAllRestrictionsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOfAllRestrictions"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO20endOfAllRestrictionsyA2CmF">endOfAllRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the end of all restrictions. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_374.svg">End of all restrictions sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOfAllRestrictions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO11generalHillyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/generalHill"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO11generalHillyA2CmF">generalHill</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a general hill. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W7-1A.svg">General hill sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">generalHill</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO14animalCrossingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/animalCrossing"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO14animalCrossingyA2CmF">animalCrossing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating animal crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_13b.svg">Animal crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">animalCrossing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13icyConditionsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/icyConditions"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13icyConditionsyA2CmF">icyConditions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating icy conditions. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-185.png">Icy conditions sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">icyConditions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO08slipperyB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/slipperyRoad"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO08slipperyB0yA2CmF">slipperyRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating slippery road. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-12.svg">Slippery road sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">slipperyRoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO12fallingRocksyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/fallingRocks"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO12fallingRocksyA2CmF">fallingRocks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating falling rocks. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_1.25.2.svg">Falling rocks sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">fallingRocks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO10schoolZoneyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/schoolZone"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO10schoolZoneyA2CmF">schoolZone</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating school zone. Example: <a href="https://en.wikipedia.org/wiki/File:Mauritius_Road_Signs_-_Warning_Sign_-_Children.svg">School zone sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">schoolZone</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15tramwayCrossingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tramwayCrossing"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15tramwayCrossingyA2CmF">tramwayCrossing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a tramway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-41.svg">Tramway crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tramwayCrossing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO16congestionHazardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/congestionHazard"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO16congestionHazardyA2CmF">congestionHazard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating congestion hazard. Example: <a href="https://en.wikipedia.org/wiki/File:Czech_Republic_road_sign_A_23.svg">Congestion hazard sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">congestionHazard</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO14accidentHazardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/accidentHazard"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO14accidentHazardyA2CmF">accidentHazard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating accident hazard. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AK31.svg">Accident hazard sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">accidentHazard</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO27priorityOverOncomingTrafficyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/priorityOverOncomingTraffic"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO27priorityOverOncomingTrafficyA2CmF">priorityOverOncomingTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating priority over oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Zeichen_308_-_Vorrang_vor_dem_Gegenverkehr,_StVO_1992.svg">Priority over oncoming traffic sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">priorityOverOncomingTraffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO22yieldToOncomingTrafficyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/yieldToOncomingTraffic"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO22yieldToOncomingTrafficyA2CmF">yieldToOncomingTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating yielding to oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_2.5.svg">Yield to oncoming traffic sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">yieldToOncomingTraffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO32crossingWithPriorityFromTheRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/crossingWithPriorityFromTheRight"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO32crossingWithPriorityFromTheRightyA2CmF">crossingWithPriorityFromTheRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating crossing with priority from the right. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AB1.svg">Crossing with priority from the right sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">crossingWithPriorityFromTheRight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO18pedestrianCrossingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrianCrossing"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO18pedestrianCrossingyA2CmF">pedestrianCrossing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating pedestrian crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_171.svg">Pedestrian crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pedestrianCrossing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO5yieldyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/yield"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO5yieldyA2CmF">yield</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating yielding. Example: <a href="https://en.wikipedia.org/wiki/File:Ontario_Wb-1A.svg">Yield sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">yield</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13doubleHairpinyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/doubleHairpin"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13doubleHairpinyA2CmF">doubleHairpin</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a double hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_W1-7-L.svg">Double hairpin sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">doubleHairpin</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13tripleHairpinyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tripleHairpin"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13tripleHairpinyA2CmF">tripleHairpin</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a triple hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_doppia_curva_sx.svg">Triple hairpin sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tripleHairpin</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO10embankmentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/embankment"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO10embankmentyA2CmF">embankment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating embankment. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-138.png">Embankment sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">embankment</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13twoWayTrafficyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/twoWayTraffic"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13twoWayTrafficyA2CmF">twoWayTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating two way traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_14.svg">Two way traffic sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">twoWayTraffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO9urbanAreayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/urbanArea"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO9urbanAreayA2CmF">urbanArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating urban area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_preavviso_intersezione.svg">Urban area sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">urbanArea</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO10humpBridgeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/humpBridge"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO10humpBridgeyA2CmF">humpBridge</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a hump bridge. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_528.svg">Hump bridge sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">humpBridge</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO06unevenB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unevenRoad"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO06unevenB0yA2CmF">unevenRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating uneven road. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_W-133.svg">Uneven road sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unevenRoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO9floodAreayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/floodArea"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO9floodAreayA2CmF">floodArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating a flood area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_zona_soggetta_ad_allagamento.svg">Flood area sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">floodArea</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO8obstacleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/obstacle"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO8obstacleyA2CmF">obstacle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating an obstacle. Example: <a href="https://en.wikipedia.org/wiki/Warning_sign#/media/File:Belgian_road_sign_A51.svg">Obstacle sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">obstacle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO04hornC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hornSign"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO04hornC0yA2CmF">hornSign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating restriction for horning. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-355.png">Horn sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hornSign</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13noEngineBrakeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noEngineBrake"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13noEngineBrakeyA2CmF">noEngineBrake</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no engine brake. Example: <a href="https://commons.wikimedia.org/wiki/File:Canada_Avoid_Engine_Brake_Sign.svg">No engine brake sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noEngineBrake</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO18endOfNoEngineBrakeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOfNoEngineBrake"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO18endOfNoEngineBrakeyA2CmF">endOfNoEngineBrake</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the end of no engine brake zone. Example: No examples available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOfNoEngineBrake</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO8noIdlingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noIdling"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO8noIdlingyA2CmF">noIdling</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no idling. Example: <a href="https://en.wikipedia.org/wiki/Idle_reduction#/media/File:Idle_free_zone_-_turn_engine_off_sign.jpg">No idling sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noIdling</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13truckRolloveryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truckRollover"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13truckRolloveryA2CmF">truckRollover</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating truck rollover. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W1-13L.svg">Truck rollover sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">truckRollover</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO7lowGearyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/lowGear"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO7lowGearyA2CmF">lowGear</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the use of low gear. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_Philippines#/media/File:Philippines_road_sign_S1-3.svg">Low gear sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">lowGear</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO12endOfLowGearyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOfLowGear"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO12endOfLowGearyA2CmF">endOfLowGear</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating the use of low gear. Example: No examples available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOfLowGear</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15bicycleCrossingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bicycleCrossing"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15bicycleCrossingyA2CmF">bicycleCrossing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating bicycles crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W6-7-FYG.svg">Bicycle crossing sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bicycleCrossing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO15yieldToBicyclesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/yieldToBicycles"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO15yieldToBicyclesyA2CmF">yieldToBicycles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating yielding to bicycles. Example: <a href="https://en.wikipedia.org/wiki/File:MK_road_sign_302.2.svg">Yield to bicycles sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">yieldToBicycles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO21noTowedCaravanAllowedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noTowedCaravanAllowed"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO21noTowedCaravanAllowedyA2CmF">noTowedCaravanAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no towed caravan allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_622.7.svg">No towed caravan allowed sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noTowedCaravanAllowed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO21noTowedTrailerAllowedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noTowedTrailerAllowed"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO21noTowedTrailerAllowedyA2CmF">noTowedTrailerAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no towed trailer allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Sweden#/media/File:Sweden_road_sign_C6.svg">No towed trailer allowed sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noTowedTrailerAllowed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO26noCamperOrMotorhomeAllowedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noCamperOrMotorhomeAllowed"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO26noCamperOrMotorhomeAllowedyA2CmF">noCamperOrMotorhomeAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no camper or motorhome allowed. Example: No examples available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noCamperOrMotorhomeAllowed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO11noTurnOnRedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noTurnOnRed"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO11noTurnOnRedyA2CmF">noTurnOnRed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating no turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:CA-QC_road_sign_P-115-1.svg">No turn on red sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noTurnOnRed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO18turnPermittedOnRedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/turnPermittedOnRed"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO18turnPermittedOnRedyA2CmF">turnPermittedOnRed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:Chile_road_sign_RA-2.svg">Turn permitted on red sign</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">turnPermittedOnRed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO12twoStageLeftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/twoStageLeft"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO12twoStageLeftyA2CmF">twoStageLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating that turning left requires a two-stage maneuver,
also known as a hook turn or Copenhagen Left, which is a special maneuver to safely
make a left turn at an intersection without crossing oncoming traffic.
This maneuver applies only in right-hand driving countries and is particularly beneficial
for cyclists, as it minimizes interaction with oncoming traffic, allowing for safer crossings. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage left turn</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">twoStageLeft</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO13twoStageRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/twoStageRight"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO13twoStageRightyA2CmF">twoStageRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A sign indicating turning right with the specified vehicle type requires a two stage maneuver.
A TWO_STAGE_RIGHT maneuver, is a special maneuver commonly used by cyclists to safely
make a right turn at an intersection without crossing oncoming traffic.
This maneuver is applicable only in left-hand driving countries and is particularly beneficial
for cyclists as they allow for safer crossings by minimizing the interaction with oncoming traffic. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage right turn</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">twoStageRight</span></code></pre>
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
