---
title: "sdk-for-ios-navigate-api-reference-structs-lanetype"
slug: "sdk-for-ios-navigate-api-reference-structs-lanetype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneType"></a>
<a title="LaneType Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        LaneType Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneType</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides information on the available lane properties.
The lane type values can be combined as follows:</p>
<ul>
<li>High Occupancy Vehicle, Reversible</li>
<li>High Occupancy Vehicle and Express</li>
<li>Reversible and Express</li>
<li>High Occupancy Vehicle, Reversible and Express</li>
<li>High Occupancy Vehicle and Acceleration</li>
<li>Reversible, Acceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Acceleration Lane</li>
<li>Express and Acceleration</li>
<li>High Occupancy Vehicle and Deceleration</li>
<li>Reversible, Deceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Deceleration Lane</li>
<li>Express and Deceleration</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isRegularSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRegular"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isRegularSbvp">isRegular</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regular lane is a lane that does not have a specific use.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRegular</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV22isHighOccupancyVehicleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isHighOccupancyVehicle"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV22isHighOccupancyVehicleSbvp">isHighOccupancyVehicle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane which is restricted for high occupancy vehicles.
Note: High occupancy vehicles are vehicles with a driver and one or more passengers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isHighOccupancyVehicle</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV12isReversibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isReversible"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV12isReversibleSbvp">isReversible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A lane in which traffic may travel in either direction, depending on certain conditions
such as the time of the day to improve traffic flow during rush hours.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isReversible</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isExpressSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isExpress"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isExpressSbvp">isExpress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Express lane is a lane or set of lanes usually physically separated from the major roadway
with limited entry and exit points to quickly move traffic in and out of a major metropolitan
city. An express lane can be reversible, bidirectional, or one-way.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isExpress</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV14isAccelerationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isAcceleration"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV14isAccelerationSbvp">isAcceleration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
increase its speed to where it can safely merge with ongoing traffic. These lanes can be
accessed from ramps, rest areas, or weigh stations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isAcceleration</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV14isDecelerationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDeceleration"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV14isDecelerationSbvp">isDeceleration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A deceleration lane is the same as an acceleration lane but used for the opposite scenario.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDeceleration</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV11isAuxiliarySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isAuxiliary"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV11isAuxiliarySbvp">isAuxiliary</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
interchange.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isAuxiliary</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV6isSlowSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isSlow"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV6isSlowSbvp">isSlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isSlow</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isPassingSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPassing"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isPassingSbvp">isPassing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A passing lane is a lane that can occur on steep mountain grades or other roads where
overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass
slow moving vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPassing</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV10isShoulderSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isShoulder"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV10isShoulderSbvp">isShoulder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
not generally used for driving, although it is possible under certain circumstances.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isShoulder</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV17isRegulatedAccessSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRegulatedAccess"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV17isRegulatedAccessSbvp">isRegulatedAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A regulated lane access is a lane designated as a holding zone, used to regulate traffic
using time intervals. Regulated lane access is only coded for truck holding zones that are
used to regulate truck access into tunnels and over bridges using time intervals (e.g., some
tunnel accesses in Switzerland).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRegulatedAccess</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV6isTurnSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTurn"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV6isTurnSbvp">isTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTurn</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV12isCenterTurnSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCenterTurn"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV12isCenterTurnSbvp">isCenterTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Center turn lane is a bidirectional turn lane located in the middle of a road that allows
traffic in both directions to turn left (right for left side driving countries).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCenterTurn</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV14isTruckParkingSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTruckParking"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV14isTruckParkingSbvp">isTruckParking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
emergency.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTruckParking</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isParkingSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isParking"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isParkingSbvp">isParking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parking lanes are portions of the road bed that may be used for parking legally. They may
allow vehicles to use them as driving lanes at times, though.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isParking</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV17isVariableDrivingSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isVariableDriving"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV17isVariableDrivingSbvp">isVariableDriving</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Variable driving lanes are lanes added to a road that open and close to accommodate traffic
volume and flow using variable indicators.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isVariableDriving</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isBicycleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBicycle"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isBicycleSbvp">isBicycle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
lane markings, signs, buffers or barriers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isBicycle</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV9isRegular0D20HighOccupancyVehicle0D10Reversible0D7Express0D12Acceleration0D12Deceleration0D9Auxiliary0D4Slow0D7Passing0D8Shoulder0D15RegulatedAccess0D4Turn0d6CenterS00D12TruckParking0dV00D15VariableDriving0D7BicycleACSb_S16btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isRegular:isHighOccupancyVehicle:isReversible:isExpress:isAcceleration:isDeceleration:isAuxiliary:isSlow:isPassing:isShoulder:isRegulatedAccess:isTurn:isCenterTurn:isTruckParking:isParking:isVariableDriving:isBicycle:)"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV9isRegular0D20HighOccupancyVehicle0D10Reversible0D7Express0D12Acceleration0D12Deceleration0D9Auxiliary0D4Slow0D7Passing0D8Shoulder0D15RegulatedAccess0D4Turn0d6CenterS00D12TruckParking0dV00D15VariableDriving0D7BicycleACSb_S16btcfc">init(isRegular:<wbr/>isHighOccupancyVehicle:<wbr/>isReversible:<wbr/>isExpress:<wbr/>isAcceleration:<wbr/>isDeceleration:<wbr/>isAuxiliary:<wbr/>isSlow:<wbr/>isPassing:<wbr/>isShoulder:<wbr/>isRegulatedAccess:<wbr/>isTurn:<wbr/>isCenterTurn:<wbr/>isTruckParking:<wbr/>isParking:<wbr/>isVariableDriving:<wbr/>isBicycle:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isRegular</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isHighOccupancyVehicle</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isReversible</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isExpress</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isAcceleration</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isDeceleration</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isAuxiliary</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isSlow</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isPassing</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isShoulder</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isRegulatedAccess</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isTurn</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isCenterTurn</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isTruckParking</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isParking</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isVariableDriving</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">isBicycle</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
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
}</HTMLBlock>
