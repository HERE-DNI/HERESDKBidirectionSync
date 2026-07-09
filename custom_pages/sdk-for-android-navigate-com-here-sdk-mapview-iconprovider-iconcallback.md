---
title: "IconProvider.IconCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IconProvider.IconCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider" title="class in com.here.sdk.mapview">IconProvider</a></dd>
</dl>
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public static interface </span><span className="element-name type-name-label">IconProvider.IconCallback</span></div>
<div className="block">Interface which is used as callback to pass back an image or error code after calling
 the createRoadShieldIcon() method.</div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="onCreateIconReply(android.graphics.Bitmap,java.lang.String,com.here.sdk.mapview.IconProviderError)">
<h3>onCreateIconReply</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onCreateIconReply</span><wbr/><span className="parameters">(@Nullable
 android.graphics.Bitmap bitmap,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovidererror" title="enum class in com.here.sdk.mapview">IconProviderError</a> error)</span></div>
<div className="block">Called when the image was created successfully or an error has occurred</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bitmap</code> - The created icon or <code>null</code> if an error occurred. Note that the
               resulting resolution of the image may differ from the width and height
               constraints because the aspect ratio is kept.</dd>
<dd><code>description</code> - A description of the created icon.</dd>
<dd><code>error</code> - Error code if icon creation failed.</dd>
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
