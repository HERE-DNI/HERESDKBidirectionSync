---
title: "CustomMetadataValue (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-custommetadatavalue"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">CustomMetadataValue</span>

</div>

<div class="block">

Interface for storing arbitrary metadata types. By implementing this
interface, multiple object types can be stored as desired, simply by
adding fields to the implementation that refer to those objects and then
assigning an instance of the CustomMetadataValue derived class to a map
item.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getTag()</code></pre></td>
  <td><div class="block">
  Obtains a tag that describes the instance of the interface.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getTag()" class="section detail">

    ### getTag

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTag</span>()

    </div>

    <div class="block">

    Obtains a tag that describes the instance of the interface. The tag
    is specific to the concrete implementation of the interface.

    </div>

    Returns:  
    A tag describing the implementation of the interface.

    </div>

  </div>

</div>

