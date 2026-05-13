---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-roadshieldiconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RoadShieldIconProperties.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadShieldIconProperties"></a>
<a title="RoadShieldIconProperties Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RoadShieldIconProperties Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadShieldIconProperties</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadShieldIconProperties</span></code></pre>
</div>
</div>
<p>Contains the information required to create a road shield image.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeType"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">routeType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of route indicating the significance of the road in a range from 0 to 6. A value of
1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-routetype">RouteType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/stateCode"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">stateCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The state code for the road. It’s a 2-letter code in ISO 3166-2 format. For example
the ones listed for US on this page <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US">https://en.wikipedia.org/wiki/ISO_3166-2:US</a>.
The code “AL” is for Alabama. Another example is the code for autonomous
communities listed on <a href="https://en.wikipedia.org/wiki/ISO_3166-2:ES">https://en.wikipedia.org/wiki/ISO_3166-2:ES</a>. Can be empty if
not required for the particular country.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV15routeNumberNameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeNumberName"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV15routeNumberNameSSvp">routeNumberName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A string that is used to additionally determine the road shield’s visual representation.
In a routing context, the text can be taken from a <code><a href="sdk-for-ios-explore-api-reference-..-structs-localizedroadnumber">LocalizedRoadNumber</a></code>, which
is available for each <code><a href="sdk-for-ios-explore-api-reference-..-classes-span">Span</a></code> of a <code><a href="sdk-for-ios-explore-api-reference-..-classes-route">Route</a></code> object.
Typically, the string contains the number of a road, such as “E100”. Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">routeType</a></code>, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">countryCode</a></code> and <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">stateCode</a></code> to identify the visual representation
of a road shield icon.</p>
<p>Note that the actual text which will be displayed on the road shield icon is set with
<code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp">RoadShieldIconProperties.shieldText</a></code>. In order to determine the visuals of the icon, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">countryCode</a></code>, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">routeType</a></code>
and eventually the <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">stateCode</a></code> is in most cases sufficient to determine the type of road
shield. In this case an empty string should be passed.</p>
<p><strong>Note:</strong> Texts that contain a <code><a href="sdk-for-ios-explore-api-reference-..-enums-cardinaldirection">CardinalDirection</a></code> are currently not supported and may lead
to unexpected results. See <code><a href="sdk-for-ios-explore-api-reference-..-structs-localizedroadnumber">LocalizedRoadNumber</a></code> for more details, it provides texts with
and without a cardinal direction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeNumberName</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/shieldText"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp">shieldText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text of the road-shield. This is the text which is displayed on the road-shield
in reality. It will be in the output road-shield icon.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">shieldText</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV9routeType11countryCode05stateI00F10NumberName10shieldTextAcA05RouteG0O_S4Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeType:countryCode:stateCode:routeNumberName:shieldText:)"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV9routeType11countryCode05stateI00F10NumberName10shieldTextAcA05RouteG0O_S4Stcfc">init(routeType:<wbr/>countryCode:<wbr/>stateCode:<wbr/>routeNumberName:<wbr/>shieldText:<wbr/>)</a>
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
<li>routeType: The type of route indicating the significance of the road in a range from 0 to 6. A value of
1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</li>
<li>countryCode: The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</li>
<li>stateCode: The state code for the road. It’s a 2-letter code in ISO 3166-2 format. For example
the ones listed for US on this page <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US">https://en.wikipedia.org/wiki/ISO_3166-2:US</a>.
The code “AL” is for Alabama. Another example is the code for autonomous
communities listed on <a href="https://en.wikipedia.org/wiki/ISO_3166-2:ES">https://en.wikipedia.org/wiki/ISO_3166-2:ES</a>. Can be empty if
not required for the particular country.</li>
<li>routeNumberName: A string that is used to additionally determine the road shield’s visual representation.
In a routing context, the text can be taken from a <code><a href="sdk-for-ios-explore-api-reference-..-structs-localizedroadnumber">LocalizedRoadNumber</a></code>, which
is available for each <code><a href="sdk-for-ios-explore-api-reference-..-classes-span">Span</a></code> of a <code><a href="sdk-for-ios-explore-api-reference-..-classes-route">Route</a></code> object.
Typically, the string contains the number of a road, such as “E100”. Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">routeType</a></code>, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">countryCode</a></code> and <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">stateCode</a></code> to identify the visual representation
of a road shield icon.</li>
</ul>
<p>Note that the actual text which will be displayed on the road shield icon is set with
  <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp">RoadShieldIconProperties.shieldText</a></code>. In order to determine the visuals of the icon, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">countryCode</a></code>, <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">routeType</a></code>
  and eventually the <code><a href="../Structs/RoadShieldIconProperties.html#/s:7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">stateCode</a></code> is in most cases sufficient to determine the type of road
  shield. In this case an empty string should be passed.</p>
<p><strong>Note:</strong> Texts that contain a <code><a href="sdk-for-ios-explore-api-reference-..-enums-cardinaldirection">CardinalDirection</a></code> are currently not supported and may lead
  to unexpected results. See <code><a href="sdk-for-ios-explore-api-reference-..-structs-localizedroadnumber">LocalizedRoadNumber</a></code> for more details, it provides texts with
  and without a cardinal direction.</p>
<ul>
<li>shieldText: The text of the road-shield. This is the text which is displayed on the road-shield
in reality. It will be in the output road-shield icon.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-routetype">RouteType</a></span><span class="p">,</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">routeNumberName</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">shieldText</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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

</div>
`
}</HTMLBlock>
