#include <stdio.h>      
#include <stdlib.h>
#include <string.h>

#define MAX_CONTACTS 100
#define NAME_LENGTH 50
#define PHONE_LENGTH 15

typedef struct {
    char name[NAME_LENGTH];
    char phone[PHONE_LENGTH];
} Contact;

void addContact(Contact contacts[], int *contactCount) {
    if (*contactCount >= MAX_CONTACTS) {
        printf("Contact list is full!\n");
        return;
    }

    printf("Enter contact name: ");
    scanf("%s", contacts[*contactCount].name);
    printf("Enter contact phone: ");
    scanf("%s", contacts[*contactCount].phone);

    (*contactCount)++;
    printf("Contact added successfully!\n");
}

void displayContacts(Contact contacts[], int contactCount) {
    if (contactCount == 0) {
        printf("No contacts to display.\n");
        return;
    }

    printf("Contact List:\n");
    for (int i = 0; i < contactCount; i++) {
        printf("Name: %s, Phone: %s\n", contacts[i].name, contacts[i].phone);
    }
}

void searchContact(Contact contacts[], int contactCount) {
    if (contactCount == 0) {
        printf("No contacts to search.\n");
        return;
    }

    char searchName[NAME_LENGTH];
    printf("Enter the name to search: ");
    scanf("%s", searchName);

    for (int i = 0; i < contactCount; i++) {
        if (strcmp(contacts[i].name, searchName) == 0) {
            printf("Contact found: Name: %s, Phone: %s\n", contacts[i].name, contacts[i].phone);
            return;
        }
    }
    printf("Contact not found.\n");
}

int main() {
    Contact contacts[MAX_CONTACTS];
    int contactCount = 0;
    int choice;

    while (1) {
        printf("\nContact Management System\n");
        printf("My name is jim");
        printf("1. Add Contact\n");
        printf("2. Display Contacts\n");
        printf("3. Search Contact\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addContact(contacts, &contactCount);
                break;
            case 2:
                displayContacts(contacts, contactCount);
                break;
            case 3:
                searchContact(contacts, contactCount);
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
