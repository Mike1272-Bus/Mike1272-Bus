// My automation : reçoit les demandes du formulaire du site.
// Chaque demande est ajoutée dans le Google Sheet et envoyée par email.
const EMAIL = 'tambwemike92@gmail.com';

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.piege) return ContentService.createTextOutput('ok'); // robot : on ignore
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  const ligne = [new Date(), p.nom || '', p.entreprise || '', p.tel || '', p.type || '', p.besoin || '', p.page || '', 'Nouveau'];
  sheet.appendRow(ligne);

  const wa = String(p.tel || '').replace(/[^0-9]/g, '');
  MailApp.sendEmail({
    to: EMAIL,
    subject: 'Nouvelle demande de démo : ' + (p.nom || '') + ' (' + (p.type || '') + ')',
    htmlBody:
      '<p><b>Nom :</b> ' + (p.nom || '') + '<br><b>Entreprise :</b> ' + (p.entreprise || '-') +
      '<br><b>WhatsApp :</b> ' + (p.tel || '') + '<br><b>Type :</b> ' + (p.type || '') +
      '<br><b>Besoin :</b> ' + (p.besoin || '-') + '</p>' +
      (wa ? '<p><a href="https://wa.me/' + wa + '">Répondre sur WhatsApp</a></p>' : '')
  });
  return ContentService.createTextOutput('ok');
}
