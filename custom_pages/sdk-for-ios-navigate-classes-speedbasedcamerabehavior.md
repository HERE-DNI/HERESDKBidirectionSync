---
title: "SpeedBasedCameraBehavior"
slug: "sdk-for-ios-navigate-classes-speedbasedcamerabehavior"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SpeedBasedCameraBehavior"></a>
<a title="SpeedBasedCameraBehavior Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        SpeedBasedCameraBehavior Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpeedBasedCameraBehavior</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SpeedBasedCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpeedBasedCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpeedBasedCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to follow the current location of the user, zooming in and out and changing
camera tilt according to the current speed.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/normalizedPrincipalPoint"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp">normalizedPrincipalPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">normalizedPrincipalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ProfileValue"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV">ProfileValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A single profile value which indicates the speed range in which it applies to its zoom and
tilt configuration.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior-profilevalue">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ProfileValue</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC10setProfileyySayAC0G5ValueVGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setProfile(_:)"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC10setProfileyySayAC0G5ValueVGF">setProfile(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the profile.
The speed ranges within the profile can overlap in order to prevent oscillations between
adjacent levels.
Provided profile must satisfy following conditions:</p>
<ul>
<li>profile must not be empty</li>
<li>each speed range must be valid (fromMetersPerSecond must be less then toMetersPerSecond)</li>
<li>ranges must be sorted by fromMetersPerSecond and toMetersPerSecond</li>
<li>gaps between ranges are not allowed
Invalid profile will be rejected and error message logged with explanation of violated restriction.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setProfile</span><span class="p">(</span><span class="n">_</span> <span class="nv">profile</span><span class="p">:</span> <span class="p">[</span><span class="kt">SpeedBasedCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>profile</em>
</code>
</td>
<td>
<div>
<p>The new profile value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC10getProfileSayAC0G5ValueVGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getProfile()"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC10getProfileSayAC0G5ValueVGyF">getProfile()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the profile.
The speed ranges within the profile can overlap in order to prevent oscillations between
adjacent levels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getProfile</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">SpeedBasedCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The profile.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC16default3DProfileSayAC12ProfileValueVGyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/default3DProfile()"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC16default3DProfileSayAC12ProfileValueVGyFZ">default3DProfile()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">default3DProfile</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">SpeedBasedCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>the default 3D profile.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC16default2DProfileSayAC12ProfileValueVGyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/default2DProfile()"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC16default2DProfileSayAC12ProfileValueVGyFZ">default2DProfile()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">default2DProfile</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">SpeedBasedCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>the default 2D profile.</p>
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
