---
title: "TileUrlProviderCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">TileUrlProviderCallback</span>

</div>

<div class="block">

Provides the URL as String for the given tile coordinates and storage
level. The first and second parameters correspond to the X and Y
coordinates of the tile, respectively, and have values ranging from 0 to
2^level − 1. The third parameter indicates the level of the tile.

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
  <td><pre><code>onTileUrlRequest(int x,
   int y,
   int level)</code></pre></td>
  <td><div class="block">
  Provides the URL as String for the given tile coordinates and storage
  level.
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

  - <div id="onTileUrlRequest(int,int,int)" class="section detail">

    ### onTileUrlRequest

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">onTileUrlRequest</span><span class="parameters">(int x,
    int y, int level)</span>

    </div>

    <div class="block">

    Provides the URL as String for the given tile coordinates and
    storage level. The first and second parameters correspond to the X
    and Y coordinates of the tile, respectively, and have values ranging
    from 0 to 2^level − 1. The third parameter indicates the level of
    the tile.

    </div>

    Parameters:  
    `x` -

    X coordinate of the tile. This ranges from 0 to 2^level − 1.

    `y` -

    Y coordinate of the tile. This ranges from 0 to 2^level − 1.

    `level` -

    Level of the tile.

    Returns:  
    the URL.

    </div>

  </div>

</div>

