---
title: "VenueMap (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuemap"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueMap.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.control.VenueMap</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueMap</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Connects a map with venues. When the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> is started,
 venues can be seen on the map as interactive models. The user can switch drawings and levels,
 change a visual style of geometries and related labels inside the venue etc.
 After constructing the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>, listeners
 for relevant events should be added to the object. <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a> is an add-on to
 the base map functionality with its own content loading and cache. For this reason, in certain
 situations there may be a small delay before the venue is visible.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<section className="detail" id="addVenueAsync(int)">
<h3>addVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueAsync</span><wbr/><span className="parameters">(int venueId)</span></div>
<div className="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addVenueAsync(java.lang.String)">
<h3>addVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueAsync</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div className="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>addVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueAsync</span><wbr/><span className="parameters">(int venueId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and add.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>addVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addVenueAsync</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>Downloads and adds a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.
 Method will do nothing if the venue already exists on the venue map.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and add.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeVenue(com.here.sdk.venue.control.Venue)">
<h3>removeVenue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeVenue</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span></div>
<div className="block"><p>Removes a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> from the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The venue to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="selectVenueAsync(int)">
<h3>selectVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">selectVenueAsync</span><wbr/><span className="parameters">(int venueId)</span></div>
<div className="block"><p>Downloads a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and select.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="selectVenueAsync(java.lang.String)">
<h3>selectVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">selectVenueAsync</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div className="block"><p>Downloads a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and select.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="selectVenueAsync(int,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>selectVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">selectVenueAsync</span><wbr/><span className="parameters">(int venueId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>Downloads a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The ID of the venue to download and select.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>selectVenueAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">selectVenueAsync</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>Downloads a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> if needed and selects a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The ID of the venue to download and select.</p></dd>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="cancelVenueSelection()">
<h3>cancelVenueSelection</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">cancelVenueSelection</span>()</div>
<div className="block"><p>Attempts to cancel venue loading and selection
 that may currently be in progress.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if a venue was about to load and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenue(com.here.sdk.core.GeoCoordinates)">
<h3>getVenue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span className="element-name">getVenue</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div className="block"><p>Tries to find a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> at the specified geographic coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where a venue is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Venue or <code>null</code> if there is no venue at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometry(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span className="element-name">getGeometry</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div className="block"><p>Tries to find a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data"><code>VenueGeometry</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the geometry is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Geometry or <code>null</code> if there is no geometry at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueLifecycleListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span></div>
<div className="block"><p>Adds a venue lifecycle listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueLifecycleListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span></div>
<div className="block"><p>Removes a venue lifecycle listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueMapLifecycleListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span></div>
<div className="block"><p>Adds a venue map lifecycle listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueMapLifecycleListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span></div>
<div className="block"><p>Removes a venue map lifecycle listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueSelectionListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span></div>
<div className="block"><p>Adds a venue selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueSelectionListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span></div>
<div className="block"><p>Removes a venue selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueDrawingSelectionListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span></div>
<div className="block"><p>Adds a drawing selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueDrawingSelectionListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span></div>
<div className="block"><p>Removes a drawing selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueLevelSelectionListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span></div>
<div className="block"><p>Adds a level selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueLevelSelectionListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span></div>
<div className="block"><p>Removes a level selection listener.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="add(com.here.sdk.venue.control.VenueInfoListListener)">
<h3>add</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">add</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span></div>
<div className="block"><p>Adds a listener to handle the completion of the asynchronous venue info list retrieval.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(com.here.sdk.venue.control.VenueInfoListListener)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span></div>
<div className="block"><p>Removes a listener for the asynchronous venue info list retrieval.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to remove.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueInfoList()">
<h3>getVenueInfoList</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</span> <span className="element-name">getVenueInfoList</span>()</div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>returns the list of object of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueInfoList(com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>getVenueInfoList</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>&gt;</span> <span className="element-name">getVenueInfoList</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback to receives the error while venue load on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>returns the list of object of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueInfoListAsync()">
<h3>getVenueInfoListAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">getVenueInfoListAsync</span>()</div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.
 Downloads the list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> asynchronously.</p></div>
</section>
</li>
<li>
<section className="detail" id="getVenueInfoListAsync(com.here.sdk.venue.control.VenueLoadErrorCallback)">
<h3>getVenueInfoListAsync</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">getVenueInfoListAsync</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span></div>
<div className="block"><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> contains venue id and name.
 Downloads the list of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data"><code>VenueInfo</code></a> asynchronously.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>Callback to receive the list of venue info if successful.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTopology(com.here.sdk.core.GeoCoordinates)">
<h3>getTopology</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></span> <span className="element-name">getTopology</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div className="block"><p>Tries to find a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data"><code>VenueTopology</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the topology is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Topology or <code>null</code> if there is no topology at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCrosswalk(com.here.sdk.core.GeoCoordinates)">
<h3>getCrosswalk</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></span> <span className="element-name">getCrosswalk</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span></div>
<div className="block"><p>Tries to find a <a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data"><code>Crosswalk</code></a> at the specified geographic coordinates
 in the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> in the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - <p>Geographic coordinates where the crosswalk is located.</p></dd>
<dt>Returns:</dt>
<dd><p>Crosswalk or <code>null</code> if there is no crosswalk at the specified geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueService()">
<h3>getVenueService</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span className="element-name">getVenueService</span>()</div>
<div className="block"><p>Gets the venue service.
 It can be used to search and get the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a> objects.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>VenueService</code> object.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSelectedVenue()">
<h3>getSelectedVenue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span className="element-name">getSelectedVenue</span>()</div>
<div className="block"><p>Gets the currently selected <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.
 Use <code>null</code> to deselect the venue.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The selected venue or <code>null</code> if no venue is selected.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSelectedVenue(com.here.sdk.venue.control.Venue)">
<h3>setSelectedVenue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setSelectedVenue</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> value)</span></div>
<div className="block"><p>Sets the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.
 Use <code>null</code> to deselect the venue.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The selected venue or <code>null</code> if no venue is selected.</p></dd>
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
