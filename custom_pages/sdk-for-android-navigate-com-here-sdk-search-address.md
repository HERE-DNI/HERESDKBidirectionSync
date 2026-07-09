---
title: "Address (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-address"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Address.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.Address</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Address</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Information about the address of a location.
 Used in <a href="sdk-for-android-navigate-place#getAddress()"><code>Place.getAddress()</code></a>.
 Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
 <code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="sdk-for-android-navigate-com-here-sdk-search-address#addressText"><code>addressText</code></a>.
 Complete address details can be obtained by searching with <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#addressText">addressText</a></code></div>
<div className="col-last even-row-color">
<div className="block">The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States".</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#block">block</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The block number for the address.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#city">city</a></code></div>
<div className="col-last even-row-color">
<div className="block">The city name for the address, for example, "Brooklyn".</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#country">country</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The country name for the address, for example, "United States".</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#countryCode">countryCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">An ISO-3166-1 (3-letter) country code for the address, for example, "USA".</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#county">county</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The county name for the address.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#district">district</a></code></div>
<div className="col-last even-row-color">
<div className="block">The district name for the address.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#houseNumOrName">houseNumOrName</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The house name or number for the address, for example, "347".</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#postalCode">postalCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The postal code for the address.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#state">state</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The state name for the address.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#stateCode">stateCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The state code for the address.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#street">street</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The street name for the address, for example, "Lewis Ave".</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#subBlock">subBlock</a></code></div>
<div className="col-last even-row-color">
<div className="block">The sub-block number for the address.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#subdistrict">subdistrict</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The subdistrict name for the address.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-addresstype" title="enum class in com.here.sdk.search">AddressType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#type">type</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the address type.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-address#%3Cinit%3E()">Address</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Default constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="city">
<h3>city</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">city</span></div>
<div className="block"><p>The city name for the address, for example, "Brooklyn".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="countryCode">
<h3>countryCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">countryCode</span></div>
<div className="block"><p>An ISO-3166-1 (3-letter) country code for the address, for example, "USA".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="country">
<h3>country</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">country</span></div>
<div className="block"><p>The country name for the address, for example, "United States".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="district">
<h3>district</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">district</span></div>
<div className="block"><p>The district name for the address.
 It is a division of city, typically an administrative unit within a larger city or
 a customary name of a city's neighborhood, for example, "Bedford-Stuyvesant".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="subdistrict">
<h3>subdistrict</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">subdistrict</span></div>
<div className="block"><p>The subdistrict name for the address.
 It is a subdivision of a district.
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="houseNumOrName">
<h3>houseNumOrName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">houseNumOrName</span></div>
<div className="block"><p>The house name or number for the address, for example, "347".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="postalCode">
<h3>postalCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">postalCode</span></div>
<div className="block"><p>The postal code for the address.
 It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally
 in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, "11233".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="state">
<h3>state</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">state</span></div>
<div className="block"><p>The state name for the address.
 It is the name of the state division of a country, for example, "New York".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="county">
<h3>county</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">county</span></div>
<div className="block"><p>The county name for the address.
 It is a division of a state, typically a secondary-level administrative division of a country or equivalent,
 for example, "Kings".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="street">
<h3>street</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">street</span></div>
<div className="block"><p>The street name for the address, for example, "Lewis Ave".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="block">
<h3>block</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">block</span></div>
<div className="block"><p>The block number for the address. It is part of Japanese addressing system.
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="subBlock">
<h3>subBlock</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">subBlock</span></div>
<div className="block"><p>The sub-block number for the address. It is part of Japanese addressing system.
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="addressText">
<h3>addressText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">addressText</span></div>
<div className="block"><p>The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-addresstype" title="enum class in com.here.sdk.search">AddressType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Specifies the address type.</p></div>
</section>
</li>
<li>
<section className="detail" id="stateCode">
<h3>stateCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">stateCode</span></div>
<div className="block"><p>The state code for the address.
 It is code/abbreviation of the state division of a country, for example, "NY".
 Note: This String can be empty when no data is available.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>Address</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Address</span>()</div>
<div className="block"><p>Default constructor.
 Note: Sets all the string values to "".</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
