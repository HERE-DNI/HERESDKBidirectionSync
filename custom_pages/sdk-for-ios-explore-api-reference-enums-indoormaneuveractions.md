---
title: "Other Enumerations / IndoorManeuverActions"
slug: "sdk-for-ios-explore-api-reference-enums-indoormaneuveractions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IndoorManeuverActions"></a>
<a title="IndoorManeuverActions Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-other%20enums">Other Enumerations</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IndoorManeuverActions Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorManeuverActions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IndoorManeuverActions</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Defines the types of actions for indoor maneuvers.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO6departyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/depart"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO6departyA2CmF">depart</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">depart</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO6arriveyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/arrive"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO6arriveyA2CmF">arrive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>End of the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">arrive</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO9leftUTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftUTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO9leftUTurnyA2CmF">leftUTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a left U-turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">leftUTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO13sharpLeftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpLeftTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO13sharpLeftTurnyA2CmF">sharpLeftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a sharp left turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sharpLeftTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO8leftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO8leftTurnyA2CmF">leftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a left turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">leftTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO14slightLeftTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/slightLeftTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO14slightLeftTurnyA2CmF">slightLeftTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a slight left turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">slightLeftTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO15slightRightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/slightRightTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO15slightRightTurnyA2CmF">slightRightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a slight right turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">slightRightTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO10continueOnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/continueOn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO10continueOnyA2CmF">continueOn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Continue on the current path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">continueOn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO9rightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO9rightTurnyA2CmF">rightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a right turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rightTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO14sharpRightTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharpRightTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO14sharpRightTurnyA2CmF">sharpRightTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a sharp right turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sharpRightTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO10rightUTurnyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightUTurn"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO10rightUTurnyA2CmF">rightUTurn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Make a right U-turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rightUTurn</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO8leftExityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leftExit"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO8leftExityA2CmF">leftExit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Exit to the left.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">leftExit</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO9rightExityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rightExit"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO9rightExityA2CmF">rightExit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Exit to the right.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rightExit</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO17levelChangeActionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/levelChangeAction"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO17levelChangeActionyA2CmF">levelChangeAction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Change level action (e.g., use stairs, elevator).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">levelChangeAction</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO11enterActionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/enterAction"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO11enterActionyA2CmF">enterAction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enter a space or area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">enterAction</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IndoorManeuverActionsO11leaveActionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/leaveAction"></a>
<a class="token" href="#/s:7heresdk21IndoorManeuverActionsO11leaveActionyA2CmF">leaveAction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Leave a space or area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">leaveAction</span></code></pre>
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
