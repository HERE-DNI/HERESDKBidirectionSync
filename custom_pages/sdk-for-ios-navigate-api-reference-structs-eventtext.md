---
title: "EventText"
slug: "sdk-for-ios-navigate-api-reference-structs-eventtext"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EventText"></a>
<a title="EventText Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        EventText Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EventText</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EventText</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains all the information regarding the next text announcement.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the type of text announcement</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-textnotificationtype">TextNotificationType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV16distanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceInMeters"></a>
<a class="token" href="#/s:7heresdk9EventTextV16distanceInMetersSdvp">distanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance in meters to the location of the event for which the text notification is given.</p>
<p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
are defined in the <code><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></code> class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV4textSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/text"></a>
<a class="token" href="#/s:7heresdk9EventTextV4textSSvp">text</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text notification instruction. The text is formatted and localized as specified via
<code><a href="sdk-for-ios-navigate-api-reference-structs-routetextoptions">RouteTextOptions</a></code>.</p>
<p><strong>Note:</strong> During navigation, the text will be always empty when the <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code> is
taken from the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code> instance via the provided index.
The text instruction that can be accessed from the <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code> instance is meant
as preview and it is not necessarily matching the more comprehensive maneuver information you
can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
texts that can be used for spoken text notifications during a trip.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">text</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV27maneuverNotificationDetailsAA08ManeuvereF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverNotificationDetails"></a>
<a class="token" href="#/s:7heresdk9EventTextV27maneuverNotificationDetailsAA08ManeuvereF0VSgvp">maneuverNotificationDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Information about the next maneuver.
Is non-<code>nil</code> only for <code><a href="../Structs/EventText.html#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp">EventText.type</a></code> equals to <code><a href="../Enums/TextNotificationType.html#/s:7heresdk20TextNotificationTypeO8maneuveryA2CmF">TextNotificationType.maneuver</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverNotificationDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationdetails">ManeuverNotificationDetails</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV26spatialNotificationDetailsAA07SpatialeF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spatialNotificationDetails"></a>
<a class="token" href="#/s:7heresdk9EventTextV26spatialNotificationDetailsAA07SpatialeF0VSgvp">spatialNotificationDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Information for a spatial text notifications.
When <code><a href="../Structs/EventTextOptions.html#/s:7heresdk16EventTextOptionsV18enableSpatialAudioSbvp">EventTextOptions.enableSpatialAudio</a></code> is false,
then this attribute will be <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spatialNotificationDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-spatialnotificationdetails">SpatialNotificationDetails</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV4type16distanceInMeters4text27maneuverNotificationDetails07spatialjK0AcA0cJ4TypeO_SdSSAA08ManeuverjK0VSgAA07SpatialjK0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:distanceInMeters:text:maneuverNotificationDetails:spatialNotificationDetails:)"></a>
<a class="token" href="#/s:7heresdk9EventTextV4type16distanceInMeters4text27maneuverNotificationDetails07spatialjK0AcA0cJ4TypeO_SdSSAA08ManeuverjK0VSgAA07SpatialjK0VSgtcfc">init(type:<wbr/>distanceInMeters:<wbr/>text:<wbr/>maneuverNotificationDetails:<wbr/>spatialNotificationDetails:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>type: Indicates the type of text announcement</li>
<li>distanceInMeters: Distance in meters to the location of the event for which the text notification is given.</li>
</ul>
<p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
  greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
  during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
  are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
  3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
  Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
  are defined in the <code><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></code> class.</p>
<ul>
<li>text: The text notification instruction. The text is formatted and localized as specified via
<code><a href="sdk-for-ios-navigate-api-reference-structs-routetextoptions">RouteTextOptions</a></code>.</li>
</ul>
<p><strong>Note:</strong> During navigation, the text will be always empty when the <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code> is
  taken from the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code> instance via the provided index.
  The text instruction that can be accessed from the <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code> instance is meant
  as preview and it is not necessarily matching the more comprehensive maneuver information you
  can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
  texts that can be used for spoken text notifications during a trip.</p>
<ul>
<li>maneuverNotificationDetails: Information about the next maneuver.
Is non-<code>nil</code> only for <code><a href="../Structs/EventText.html#/s:7heresdk9EventTextV4typeAA0C16NotificationTypeOvp">EventText.type</a></code> equals to <code><a href="../Enums/TextNotificationType.html#/s:7heresdk20TextNotificationTypeO8maneuveryA2CmF">TextNotificationType.maneuver</a></code>.</li>
<li>spatialNotificationDetails: Information for a spatial text notifications.
When <code><a href="../Structs/EventTextOptions.html#/s:7heresdk16EventTextOptionsV18enableSpatialAudioSbvp">EventTextOptions.enableSpatialAudio</a></code> is false,
then this attribute will be <code>nil</code>.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-textnotificationtype">TextNotificationType</a></span><span class="p">,</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">text</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">maneuverNotificationDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-maneuvernotificationdetails">ManeuverNotificationDetails</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">spatialNotificationDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-spatialnotificationdetails">SpatialNotificationDetails</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
