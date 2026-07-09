---
title: "WarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warninglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- WarningListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">WarningListener</span></div>
<div className="block"><p>A generic listener interface interface for receiving warning notifications.
 Implementations of this interface are notified whenever the <code>WarnerEngine</code> detects new warnings.
 The listener receives a list of <code>Warning</code> objects, each describing a specific event or condition that requires user attention.
 Classes interested in warning updates should implement this listener
 and register themselves via <code>WarnerEngine.addWarningListener</code>.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="onWarnings(java.util.List)">
<h3>onWarnings</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onWarnings</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a>&gt; warnings)</span></div>
<div className="block"><p>Called when a new warnings is detected.
 This method is invoked whenever a new list of warnings becomes available.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warnings</code> - <p>The list of warning objects containing details about each warning.</p></dd>
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
