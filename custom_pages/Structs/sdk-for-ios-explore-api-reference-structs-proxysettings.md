---
title: "ProxySettings Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-proxysettings"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ProxySettings.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ProxySettings"></a>
<a title="ProxySettings Structure Reference"></a>
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
<a href="../Core.html">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ProxySettings Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ProxySettings : Hashable</code></pre>
</div>
</div>
<p>Proxy configuration for the HERE SDK network that is applied per request.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV4typeAC0B4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV4typeAC0B4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the type of the proxy server.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var type: ProxySettings.ProxyType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV9ipAddress7Network9IPAddress_pvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ipAddress"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV9ipAddress7Network9IPAddress_pvp">ipAddress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the IP Address of the proxy server.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var ipAddress: IPAddress</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV4ports6UInt16Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/port"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV4ports6UInt16Vvp">port</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the port number of the proxy server.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var port: UInt16</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV11credentialsAC11CredentialsVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/credentials"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV11credentialsAC11CredentialsVSgvp">credentials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional field to define credentials to authenticate a user to the proxy server.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var credentials: ProxySettings.Credentials?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV4type9ipAddress4port11credentialsA2C0B4TypeO_7Network9IPAddress_ps6UInt16VAC11CredentialsVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:ipAddress:port:credentials:)"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV4type9ipAddress4port11credentialsA2C0B4TypeO_7Network9IPAddress_ps6UInt16VAC11CredentialsVSgtcfc">init(type:<wbr/>ipAddress:<wbr/>port:<wbr/>credentials:<wbr/>)</a>
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
<pre><code>public init(type: ProxySettings.ProxyType, ipAddress: IPAddress, port: UInt16, credentials: ProxySettings.Credentials? = nil)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV0B4TypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ProxyType"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV0B4TypeO">ProxyType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supported types of proxy connection.</p>
<a class="slightly-smaller" href="../Structs/ProxySettings/ProxyType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum ProxyType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV11CredentialsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Credentials"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV11CredentialsV">Credentials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authentication data</p>
<a class="slightly-smaller" href="../Structs/ProxySettings/Credentials.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Credentials : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV2eeoiySbAC_ACtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/==(_:_:)"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV2eeoiySbAC_ACtFZ">==(_:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Compare objects</p>
<ul>
<li>Return true if objects are equal, false otherwise.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>static func == (lhs: ProxySettings, rhs: ProxySettings) -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lhs</em>
</code>
</td>
<td>
<div>
<p>First object to compare</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rhs</em>
</code>
</td>
<td>
<div>
<p>Second object to compare</p>
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
<a name="/s:7heresdk13ProxySettingsV4hash4intoys6HasherVz_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/hash(into:)"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV4hash4intoys6HasherVz_tF">hash(into:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hashes object</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>func hash(into hasher: inout Hasher)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>hasher</em>
</code>
</td>
<td>
<div>
<p>The hasher</p>
</div>
</td>
</tr>
</tbody>
</table>
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
