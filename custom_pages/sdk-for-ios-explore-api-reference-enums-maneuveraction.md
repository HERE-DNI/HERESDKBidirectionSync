---
title: "ManeuverAction Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-maneuveraction"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ManeuverAction.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/ManeuverAction"></a>
<a title="ManeuverAction Enumeration Reference"></a>
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
        ManeuverAction Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum ManeuverAction : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Maneuver action type.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO6departyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/depart"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO6departyA2CmF">depart</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Departure maneuver, such as “Head towards”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case depart</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO6arriveyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/arrive"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO6arriveyA2CmF">arrive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Arrival maneuver, such as “You have reached your destination/waypoint”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case arrive</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO9leftUTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftUTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO9leftUTurnyA2CmF">leftUTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Left-hand U-turn maneuver, such as “Make a U-turn”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftUTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO13sharpLeftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpLeftTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO13sharpLeftTurnyA2CmF">sharpLeftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sharp left turn maneuver, such as “Turn sharply left”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case sharpLeftTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO8leftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO8leftTurnyA2CmF">leftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Left turn maneuver, such as “Turn left”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO14slightLeftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/slightLeftTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO14slightLeftTurnyA2CmF">slightLeftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Slight left turn maneuver, such as “Turn slightly left”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case slightLeftTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO10continueOnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/continueOn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO10continueOnyA2CmF">continueOn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Continue maneuver, such as “Continue straight ahead”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case continueOn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO15slightRightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/slightRightTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO15slightRightTurnyA2CmF">slightRightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Slight right turn maneuver, such as “Turn slightly right”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case slightRightTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO9rightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO9rightTurnyA2CmF">rightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Right turn maneuver, such as “Turn right”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO14sharpRightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpRightTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO14sharpRightTurnyA2CmF">sharpRightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sharp right turn maneuver, such as “Turn sharply right”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case sharpRightTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO10rightUTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightUTurn"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO10rightUTurnyA2CmF">rightUTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Right u-turn maneuver, such as “Make a U-turn”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightUTurn</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO8leftExityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftExit"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO8leftExityA2CmF">leftExit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Left exit maneuver, such as “Take the exit”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftExit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO9rightExityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightExit"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO9rightExityA2CmF">rightExit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Right exit maneuver, such as “Take the exit”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightExit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO8leftRampyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRamp"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO8leftRampyA2CmF">leftRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Left ramp maneuver, such as “Join the highway”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRamp</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO9rightRampyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRamp"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO9rightRampyA2CmF">rightRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Right ramp maneuver, such as “Join the highway”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRamp</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO8leftForkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftFork"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO8leftForkyA2CmF">leftFork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Left fork maneuver, such as “Keep left”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftFork</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO10middleForkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/middleFork"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO10middleForkyA2CmF">middleFork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Middle fork maneuver, such as “Keep middle”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case middleFork</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO9rightForkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightFork"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO9rightForkyA2CmF">rightFork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Right fork maneuver, such as “Keep right”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightFork</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20enterHighwayFromLeftyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/enterHighwayFromLeft"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20enterHighwayFromLeftyA2CmF">enterHighwayFromLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Merge onto a highway from the left side. Such a maneuver occurs only in countries that drive on the left side of the road (left-hand traffic).</p>
<p><strong>Note:</strong> This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0,
it needs to be enabled via <code><a href="sdk-for-ios-explore-api-reference-..-structs-routeoptions">RouteOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case enterHighwayFromLeft</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO21enterHighwayFromRightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/enterHighwayFromRight"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO21enterHighwayFromRightyA2CmF">enterHighwayFromRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Merge onto a highway from the right side. Such a maneuver occurs only in countries that drive on the right side of the road (right-hand traffic).</p>
<p><strong>Note:</strong> This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0,
it needs to be enabled via <code><a href="sdk-for-ios-explore-api-reference-..-structs-routeoptions">RouteOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case enterHighwayFromRight</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutEnteryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutEnter"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutEnteryA2CmF">leftRoundaboutEnter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Enter the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutEnter</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutEnteryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutEnter"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutEnteryA2CmF">rightRoundaboutEnter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Enter the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutEnter</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO18leftRoundaboutPassyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutPass"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO18leftRoundaboutPassyA2CmF">leftRoundaboutPass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Pass the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutPass</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19rightRoundaboutPassyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutPass"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19rightRoundaboutPassyA2CmF">rightRoundaboutPass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Pass the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutPass</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit1yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit1"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit1yA2CmF">leftRoundaboutExit1</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as  “Take the first exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit1</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit2yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit2"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit2yA2CmF">leftRoundaboutExit2</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the second exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit2</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit3yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit3"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit3yA2CmF">leftRoundaboutExit3</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the third exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit3</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit4yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit4"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit4yA2CmF">leftRoundaboutExit4</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the fourth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit4</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit5yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit5"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit5yA2CmF">leftRoundaboutExit5</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the fifth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit5</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit6yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit6"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit6yA2CmF">leftRoundaboutExit6</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the sixth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit6</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit7yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit7"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit7yA2CmF">leftRoundaboutExit7</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the seventh exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit7</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit8yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit8"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit8yA2CmF">leftRoundaboutExit8</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the eighth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit8</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO19leftRoundaboutExit9yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit9"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO19leftRoundaboutExit9yA2CmF">leftRoundaboutExit9</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the ninth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit9</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20leftRoundaboutExit10yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit10"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20leftRoundaboutExit10yA2CmF">leftRoundaboutExit10</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the tenth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit10</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20leftRoundaboutExit11yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit11"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20leftRoundaboutExit11yA2CmF">leftRoundaboutExit11</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the eleventh exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit11</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20leftRoundaboutExit12yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftRoundaboutExit12"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20leftRoundaboutExit12yA2CmF">leftRoundaboutExit12</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (left-hand traffic), such as “Take the twelfth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case leftRoundaboutExit12</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit1yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit1"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit1yA2CmF">rightRoundaboutExit1</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the first exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit1</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit2yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit2"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit2yA2CmF">rightRoundaboutExit2</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the second exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit2</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit3yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit3"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit3yA2CmF">rightRoundaboutExit3</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the third exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit3</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit4yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit4"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit4yA2CmF">rightRoundaboutExit4</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the fourth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit4</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit5yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit5"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit5yA2CmF">rightRoundaboutExit5</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the fifth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit5</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit6yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit6"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit6yA2CmF">rightRoundaboutExit6</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the sixth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit6</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit7yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit7"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit7yA2CmF">rightRoundaboutExit7</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the seventh exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit7</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit8yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit8"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit8yA2CmF">rightRoundaboutExit8</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the eighth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit8</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO20rightRoundaboutExit9yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit9"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO20rightRoundaboutExit9yA2CmF">rightRoundaboutExit9</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the ninth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit9</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO21rightRoundaboutExit10yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit10"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO21rightRoundaboutExit10yA2CmF">rightRoundaboutExit10</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the tenth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit10</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO21rightRoundaboutExit11yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit11"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO21rightRoundaboutExit11yA2CmF">rightRoundaboutExit11</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the eleventh exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit11</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ManeuverActionO21rightRoundaboutExit12yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightRoundaboutExit12"></a>
<a class="token" href="#/s:7heresdk14ManeuverActionO21rightRoundaboutExit12yA2CmF">rightRoundaboutExit12</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Roundabout maneuver (right-hand traffic), such as “Take the twelfth exit at the roundabout”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rightRoundaboutExit12</code></pre>
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
