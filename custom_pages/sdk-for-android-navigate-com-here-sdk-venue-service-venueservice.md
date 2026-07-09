---
title: "VenueService (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venueservice"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueService.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.service</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.service.VenueService</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueService</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Offers methods to download venues. Use of this
 object does not necessitate Map involvement.
 
 Before loading the venues, initialize the venue service
 with one of the start methods.

 
 The venue service is online only. Even if there is a cached
 venue on the device, the venue service requires an online
 connection to check if the venue is available for the user.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice-venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional features enum</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="stop()">
<h3>stop</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">stop</span>()</div>
<div className="block"><p>Stops the venue service.</p></div>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.service.VenueServiceListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span></div>
<div className="block"><p>Adds a service listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The service listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.service.VenueServiceListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span></div>
<div className="block"><p>Removes a service listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The service listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.service.VenueListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span></div>
<div className="block"><p>Adds a venue listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.service.VenueListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span></div>
<div className="block"><p>Removes a venue listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.service.VenueMapListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span></div>
<div className="block"><p>Adds a venue map listener. The listener
 is not added if it is <code>null</code> or is already present in the list of
 listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue map listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.service.VenueMapListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span></div>
<div className="block"><p>Removes a venue map listener. The listener
 is not removed if it is not present in the list of listeners.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The venue map listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInitStatus()">
<h3>getInitStatus</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">VenueServiceInitStatus</a></span> <span className="element-name">getInitStatus</span>()</div>
<div className="block"><p>Gets an initialization status.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The initialization status.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isInitialized()">
<h3>isInitialized</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isInitialized</span>()</div>
<div className="block"><p>Checks if the venue service is initialized.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if the venue service is initialized and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addVenueToLoad(int)">
<h3>addVenueToLoad</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueToLoad</span><wbr/><span className="parameters">(int venueId)</span></div>
<div className="block"><p>Adds a venue to the loading queue.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The id of the venue to load.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addVenueToLoad(java.lang.String)">
<h3>addVenueToLoad</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueToLoad</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div className="block"><p>Adds a venue to the loading queue.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The id of the venue to load.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setHrn(java.lang.String)">
<h3>setHrn</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setHrn</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hrn)</span></div>
<div className="block"><p>Sets HRN of platform catalog.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>hrn</code> - <p>The HRN of platform catalog.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLabeltextPreference(java.util.List)">
<h3>setLabeltextPreference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setLabeltextPreference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; labelTextPref)</span></div>
<div className="block"><p>Sets override labelTextPreference for labels.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>labelTextPref</code> - <p>The list of string override labelTextPreference.
     
     "OCCUPANT_NAMES" - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348

     
     "SPACE_NAME" - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348

     
     "SPACE_TYPE_NAME" - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348

     
     "SPACE_CATEGORY_NAME" - To display only space categories on map as a label text. Example: SAFETY for id 7348

     
     "INTERNAL_ADDRESS" - To display only internal addresses on map as a label text. Example: 51/D for id 7348</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadTopologies()">
<h3>loadTopologies</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadTopologies</span>()</div>
<div className="block"><p>Lets user load topologies for current session</p></div>
</section>
</li>
<li>
<section className="detail" id="loadOptionalFeatures(java.util.List)">
<h3>loadOptionalFeatures</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadOptionalFeatures</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice-venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a>&gt; optionalFeatureList)</span></div>
<div className="block"><p>Lets user load optional features for current session.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optionalFeatureList</code> - <p>The list of optional feature enum VenueOptionalFeature.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLanguages()">
<h3>getLanguages</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">getLanguages</span>()</div>
<div className="block"><p>Gets the languages available in the venue service.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The languages available in the venue service.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getLanguage</span>()</div>
<div className="block"><p>Gets an active language in the venue service.
 The venue service will try to load
 a venue with a translation in the active language. If such translation doesn't
 exist, a venue will be loaded in its default language.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The active language.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setLanguage(java.lang.String)">
<h3>setLanguage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setLanguage</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Sets an active language.
 The venue service will try to load
 a venue with a translation in the active language. If such translation doesn't
 exist, a venue will be loaded in its default language.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The active language.</p></dd>
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
