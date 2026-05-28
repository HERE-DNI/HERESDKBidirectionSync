---
title: "Other Structures / DriveRestRegulation"
slug: "sdk-for-ios-navigate-api-reference-structs-driverestregulation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DriveRestRegulation"></a>
<a title="DriveRestRegulation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-other%20structs">Other Structures</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DriveRestRegulation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DriveRestRegulation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DriveRestRegulation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Drive-rest regulation defining mandatory rest requirements for commercial vehicle drivers.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxDailyDriveTimeInMinutes"></a>
<a class="token" href="#/s:7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutesSdSgvp">maxDailyDriveTimeInMinutes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum continuous or accumulated daily driving time in minutes before a rest is required.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxDailyDriveTimeInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19DriveRestRegulationV05dailyC12MinInMinutesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dailyRestMinInMinutes"></a>
<a class="token" href="#/s:7heresdk19DriveRestRegulationV05dailyC12MinInMinutesSdSgvp">dailyRestMinInMinutes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum daily rest duration in minutes that must be taken.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dailyRestMinInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19DriveRestRegulationV03midbC9InMinutesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/midDriveRestInMinutes"></a>
<a class="token" href="#/s:7heresdk19DriveRestRegulationV03midbC9InMinutesSdSgvp">midDriveRestInMinutes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum driving time in minutes allowed before a mid-drive rest must be taken.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">midDriveRestInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19DriveRestRegulationV03midbC12MinInMinutesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/midDriveRestMinInMinutes"></a>
<a class="token" href="#/s:7heresdk19DriveRestRegulationV03midbC12MinInMinutesSdSgvp">midDriveRestMinInMinutes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum duration in minutes of the required mid-drive rest.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">midDriveRestMinInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutes05dailyc3MinhI003midbchI00lbckhI0ACSdSg_A3Htcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maxDailyDriveTimeInMinutes:dailyRestMinInMinutes:midDriveRestInMinutes:midDriveRestMinInMinutes:)"></a>
<a class="token" href="#/s:7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutes05dailyc3MinhI003midbchI00lbckhI0ACSdSg_A3Htcfc">init(maxDailyDriveTimeInMinutes:<wbr/>dailyRestMinInMinutes:<wbr/>midDriveRestInMinutes:<wbr/>midDriveRestMinInMinutes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maxDailyDriveTimeInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">dailyRestMinInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">midDriveRestInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">midDriveRestMinInMinutes</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
