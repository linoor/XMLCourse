<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <html>
      <body>
      <h2>Cennik</h2>
      <table border="1">
        <tr bgcolor="#0cb4ce">
          <th>marka</th>
          <th>model</th>
          <th>rocznik</th>
          <th>numer katalogowy</th>
          <th>cena</th>
        </tr>
        <xsl:for-each select="cennik/samochod">
        <tr>
          <td><xsl:value-of select="marka"/></td>
          <td><xsl:value-of select="model"/></td>
          <td><xsl:value-of select="rocznik"/></td>
          <td><xsl:value-of select="num_kat"/></td>
          <td><xsl:value-of select="cena"/></td>
        </tr>
        </xsl:for-each>
      </table>
      </body>
      </html>
    </xsl:template>
</xsl:stylesheet>