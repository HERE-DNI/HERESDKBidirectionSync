---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-administrativerulesloader"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AdministrativeRulesLoader.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/AdministrativeRulesLoader"></a>
<a title="AdministrativeRulesLoader Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AdministrativeRulesLoader Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AdministrativeRulesLoader</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AdministrativeRulesLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AdministrativeRulesLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AdministrativeRulesLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides the protocol for the access to the administrative rules available
for a country or a state in the local OCM map. Please be aware that the methods within this
classload map data synchronously. In the event of absent data in the disk cache, the data
will be retrieved from the remote server. To mitigate the potential freezing of the calling
thread, it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25AdministrativeRulesLoaderCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk25AdministrativeRulesLoaderCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25AdministrativeRulesLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk25AdministrativeRulesLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>A SDKEngine instance.</p>
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
<a name="/s:7heresdk25AdministrativeRulesLoaderC13getStateCodes11countryCodeSaySSGAA07CountryI0O_tKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getStateCodes(countryCode:)"></a>
<a class="token" href="#/s:7heresdk25AdministrativeRulesLoaderC13getStateCodes11countryCodeSaySSGAA07CountryI0O_tKF">getStateCodes(countryCode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Synchronously loads the list of state codes from a specified country for which
administrative rules are availabe. These state codes can then be used to get specific
administrative rules for a specified state using the <code>get_administrative_rules()</code> method.
Returns a list with all the state codes available in the country. In case the country has no
states, the list will be empty.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why the list of state codes was not returned.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getStateCodes</span><span class="p">(</span><span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-countrycode">CountryCode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>countryCode</em>
</code>
</td>
<td>
<div>
<p>The country code for which the state codes are going to be retrieved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The list of state codes present in the country for which administrative rules
are available.
Throws if it’s not possible to return the list of state codes.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25AdministrativeRulesLoaderC03getbC011countryCode05stateG0AA0bC0VAA07CountryG0O_SSSgtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAdministrativeRules(countryCode:stateCode:)"></a>
<a class="token" href="#/s:7heresdk25AdministrativeRulesLoaderC03getbC011countryCode05stateG0AA0bC0VAA07CountryG0O_SSSgtKF">getAdministrativeRules(countryCode:<wbr/>stateCode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Synchronously load the administrative rules for the specified country and state.
<strong>Note:</strong> The <code>state_code</code> parameter can be set to <code>nil</code>. In this case, even if the country has multiple states, each with
their own administrative rules, an <code><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></code> object will be returned, containing the administrative
rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that
specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy.
Returns an <code><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></code> object which contains the administrative rules for the specified country and
state.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapData.html#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a></code> Specifies reason, why the administrative rules were not retrieved.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getAdministrativeRules</span><span class="p">(</span><span class="nv">countryCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-countrycode">CountryCode</a></span><span class="p">,</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-administrativerules">AdministrativeRules</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>countryCode</em>
</code>
</td>
<td>
<div>
<p>The country code for which the administrative rules will be retrieved.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>stateCode</em>
</code>
</td>
<td>
<div>
<p>The state name for which the administrative rules will be received. It can be <code>nil</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Requested administrative rules for the country and the state specified.</p>
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
